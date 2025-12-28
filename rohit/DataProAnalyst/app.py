from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import numpy as np
import os
import io
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import traceback
import webbrowser
import threading

# Data processing modules
from data_processing import DataCleaner, DataAnalyzer, DataModeler, DataVisualizer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

# Store current dataframe in session
current_data = {}

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only CSV and Excel files allowed'}), 400
        
        # Save and read file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Read data
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        else:
            df = pd.read_excel(filepath)
        
        # Store in session
        current_data['df'] = df
        current_data['filename'] = filename
        current_data['filepath'] = filepath
        
        # Get preview data
        preview = {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.astype(str).to_dict(),
            'head': df.head(10).to_dict('records'),
            'missing': df.isnull().sum().to_dict()
        }
        
        return jsonify({
            'success': True,
            'message': f'File uploaded successfully: {filename}',
            'preview': preview
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error uploading file: {str(e)}'}), 500

@app.route('/api/data-preview', methods=['GET'])
def get_data_preview():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        df = current_data['df']
        return jsonify({
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.astype(str).to_dict(),
            'head': df.head(10).to_html(),
            'stats': df.describe().to_dict()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clean-data', methods=['POST'])
def clean_data():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        data = request.json
        df = current_data['df'].copy()
        
        cleaner = DataCleaner(df)
        
        # Apply cleaning operations
        if data.get('handle_missing'):
            method = data.get('missing_method', 'drop')
            df = cleaner.handle_missing_values(method=method)
        
        if data.get('remove_duplicates'):
            df = cleaner.remove_duplicates()
        
        if data.get('handle_outliers'):
            df = cleaner.handle_outliers(method=data.get('outlier_method', 'iqr'))
        
        if data.get('normalize'):
            columns = data.get('normalize_columns', [])
            if columns:
                df = cleaner.normalize_data(columns=columns)
        
        # Store cleaned data
        current_data['df_cleaned'] = df
        
        return jsonify({
            'success': True,
            'message': 'Data cleaned successfully',
            'shape': df.shape,
            'preview': df.head(10).to_dict('records'),
            'missing': df.isnull().sum().to_dict()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/eda', methods=['POST'])
def exploratory_analysis():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        df = current_data.get('df_cleaned', current_data['df'])
        analyzer = DataAnalyzer(df)
        
        # Get EDA results
        stats = analyzer.get_summary_statistics()
        correlations = analyzer.get_correlations()
        distributions = analyzer.get_distributions()
        
        return jsonify({
            'success': True,
            'stats': stats,
            'correlations': correlations,
            'distributions': distributions
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/model', methods=['POST'])
def build_model():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        data = request.json
        df = current_data.get('df_cleaned', current_data['df'])
        
        task_type = data.get('task_type')
        target_column = data.get('target_column')
        
        if not target_column or target_column not in df.columns:
            return jsonify({'error': 'Invalid target column'}), 400
        
        modeler = DataModeler(df)
        
        if task_type == 'regression':
            result = modeler.build_regression_model(target_column)
        elif task_type == 'classification':
            result = modeler.build_classification_model(target_column)
        elif task_type == 'clustering':
            n_clusters = data.get('n_clusters', 3)
            result = modeler.build_clustering_model(n_clusters=n_clusters)
        else:
            return jsonify({'error': 'Unknown task type'}), 400
        
        current_data['model_result'] = result
        
        return jsonify({
            'success': True,
            'task_type': task_type,
            'result': result
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/visualize', methods=['POST'])
def create_visualization():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        data = request.json
        df = current_data.get('df_cleaned', current_data['df'])
        
        viz_type = data.get('viz_type')
        columns = data.get('columns', [])
        color = data.get('color', '#1f77b4')
        title = data.get('title', f'{viz_type} Chart')
        
        visualizer = DataVisualizer(df)
        
        if viz_type == 'scatter':
            if len(columns) >= 2:
                fig_html = visualizer.create_scatter(columns[0], columns[1], color=color, title=title)
            else:
                return jsonify({'error': 'Scatter plot needs 2 columns'}), 400
        
        elif viz_type == 'bar':
            if len(columns) >= 1:
                fig_html = visualizer.create_bar(columns[0], color=color, title=title)
            else:
                return jsonify({'error': 'Bar chart needs at least 1 column'}), 400
        
        elif viz_type == 'histogram':
            if len(columns) >= 1:
                fig_html = visualizer.create_histogram(columns[0], color=color, title=title)
            else:
                return jsonify({'error': 'Histogram needs at least 1 column'}), 400
        
        elif viz_type == 'heatmap':
            fig_html = visualizer.create_heatmap()
        
        elif viz_type == 'line':
            if len(columns) >= 2:
                fig_html = visualizer.create_line(columns[0], columns[1], color=color, title=title)
            else:
                return jsonify({'error': 'Line chart needs 2 columns'}), 400
        
        elif viz_type == 'box':
            if len(columns) >= 1:
                fig_html = visualizer.create_boxplot(columns, title=title)
            else:
                return jsonify({'error': 'Box plot needs at least 1 column'}), 400
        
        else:
            return jsonify({'error': 'Unknown visualization type'}), 400
        
        return jsonify({
            'success': True,
            'chart': fig_html
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/export-data', methods=['GET'])
def export_data():
    try:
        if 'df_cleaned' not in current_data:
            return jsonify({'error': 'No cleaned data to export'}), 400
        
        df = current_data['df_cleaned']
        filename = f"cleaned_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
        
        df.to_csv(filepath, index=False)
        
        return send_file(
            filepath,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/export-visualization', methods=['POST'])
def export_visualization():
    try:
        data = request.json
        viz_type = data.get('viz_type')
        
        df = current_data.get('df_cleaned', current_data['df'])
        visualizer = DataVisualizer(df)
        
        filename = f"viz_{viz_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
        
        # Create and save visualization
        visualizer.save_visualization(viz_type, filepath, data)
        
        return send_file(
            filepath,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/columns', methods=['GET'])
def get_columns():
    try:
        if 'df' not in current_data:
            return jsonify({'error': 'No data loaded'}), 400
        
        df = current_data['df']
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        all_cols = df.columns.tolist()
        
        return jsonify({
            'numeric': numeric_cols,
            'all': all_cols
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_data():
    current_data.clear()
    return jsonify({'success': True, 'message': 'Data cleared'}), 200

def open_browser():
    """Open browser after a delay to ensure server is ready"""
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Start browser in a separate thread with a small delay
    timer = threading.Timer(1.5, open_browser)
    timer.daemon = True
    timer.start()
    
    app.run(debug=True, host='127.0.0.1', port=5000, threaded=True, use_reloader=False)
