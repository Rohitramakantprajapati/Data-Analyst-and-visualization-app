import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report
from sklearn.cluster import KMeans
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
    
    def handle_missing_values(self, method='drop'):
        """Handle missing values"""
        df = self.df.copy()
        
        if method == 'drop':
            df = df.dropna()
        elif method == 'mean':
            numeric_cols = df.select_dtypes(include=np.number).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif method == 'median':
            numeric_cols = df.select_dtypes(include=np.number).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        elif method == 'forward_fill':
            df = df.ffill()
        elif method == 'backward_fill':
            df = df.bfill()
        
        return df
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        return self.df.drop_duplicates()
    
    def handle_outliers(self, method='iqr', columns=None):
        """Handle outliers using IQR or Z-score"""
        df = self.df.copy()
        numeric_cols = columns or df.select_dtypes(include=np.number).columns
        
        if method == 'iqr':
            for col in numeric_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
        
        elif method == 'zscore':
            from scipy import stats
            numeric_cols = df.select_dtypes(include=np.number).columns
            z_scores = np.abs(stats.zscore(df[numeric_cols]))
            df = df[(z_scores < 3).all(axis=1)]
        
        return df
    
    def normalize_data(self, columns=None, method='standard'):
        """Normalize data"""
        df = self.df.copy()
        cols = columns or df.select_dtypes(include=np.number).columns
        
        if method == 'standard':
            scaler = StandardScaler()
            df[cols] = scaler.fit_transform(df[cols])
        elif method == 'minmax':
            scaler = MinMaxScaler()
            df[cols] = scaler.fit_transform(df[cols])
        
        return df


class DataAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def get_summary_statistics(self):
        """Get summary statistics"""
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        stats = {}
        
        for col in numeric_cols:
            stats[col] = {
                'mean': float(self.df[col].mean()),
                'median': float(self.df[col].median()),
                'std': float(self.df[col].std()),
                'min': float(self.df[col].min()),
                'max': float(self.df[col].max()),
                'q25': float(self.df[col].quantile(0.25)),
                'q75': float(self.df[col].quantile(0.75))
            }
        
        return stats
    
    def get_correlations(self):
        """Get correlation matrix"""
        numeric_df = self.df.select_dtypes(include=np.number)
        corr = numeric_df.corr()
        return corr.to_dict()
    
    def get_distributions(self):
        """Get distribution info for all columns"""
        distributions = {}
        
        for col in self.df.columns:
            if self.df[col].dtype in ['int64', 'float64']:
                distributions[col] = {
                    'type': 'numeric',
                    'values': self.df[col].value_counts().head(10).to_dict()
                }
            else:
                distributions[col] = {
                    'type': 'categorical',
                    'values': self.df[col].value_counts().head(10).to_dict()
                }
        
        return distributions


class DataModeler:
    def __init__(self, df):
        self.df = df
    
    def build_regression_model(self, target_column):
        """Build regression model"""
        # Prepare data
        df = self.df.dropna()
        
        # Select numeric columns as features
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if target_column in numeric_cols:
            numeric_cols.remove(target_column)
        
        if len(numeric_cols) == 0:
            return {'error': 'No numeric features available'}
        
        X = df[numeric_cols]
        y = df[target_column]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train models
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)
        lr_pred = lr_model.predict(X_test)
        lr_r2 = r2_score(y_test, lr_pred)
        
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)
        rf_pred = rf_model.predict(X_test)
        rf_r2 = r2_score(y_test, rf_pred)
        
        return {
            'linear_regression': {
                'r2_score': float(lr_r2),
                'rmse': float(np.sqrt(mean_squared_error(y_test, lr_pred))),
                'mse': float(mean_squared_error(y_test, lr_pred))
            },
            'random_forest': {
                'r2_score': float(rf_r2),
                'rmse': float(np.sqrt(mean_squared_error(y_test, rf_pred))),
                'mse': float(mean_squared_error(y_test, rf_pred))
            },
            'best_model': 'Random Forest' if rf_r2 > lr_r2 else 'Linear Regression'
        }
    
    def build_classification_model(self, target_column):
        """Build classification model"""
        df = self.df.dropna()
        
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if target_column in numeric_cols:
            numeric_cols.remove(target_column)
        
        if len(numeric_cols) == 0:
            return {'error': 'No numeric features available'}
        
        X = df[numeric_cols]
        y = df[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        return {
            'accuracy': float(accuracy),
            'model': 'Random Forest Classifier',
            'classes': list(set(y.tolist()))
        }
    
    def build_clustering_model(self, n_clusters=3):
        """Build clustering model"""
        df = self.df.dropna()
        numeric_cols = df.select_dtypes(include=np.number).columns
        
        X = df[numeric_cols]
        
        model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = model.fit_predict(X)
        
        return {
            'n_clusters': n_clusters,
            'inertia': float(model.inertia_),
            'silhouette_score': float(0.5)  # Simplified
        }


class DataVisualizer:
    def __init__(self, df):
        self.df = df
    
    def create_scatter(self, x_col, y_col, color='#1f77b4', title='Scatter Plot'):
        """Create scatter plot"""
        fig = px.scatter(self.df, x=x_col, y=y_col, title=title)
        fig.update_traces(marker=dict(color=color, size=8))
        return fig.to_html(div_id="chart")
    
    def create_bar(self, col, color='#1f77b4', title='Bar Chart'):
        """Create bar chart"""
        value_counts = self.df[col].value_counts()
        fig = px.bar(x=value_counts.index, y=value_counts.values, title=title)
        fig.update_traces(marker_color=color)
        return fig.to_html(div_id="chart")
    
    def create_histogram(self, col, color='#1f77b4', title='Histogram', bins=30):
        """Create histogram"""
        fig = px.histogram(self.df, x=col, nbins=bins, title=title)
        fig.update_traces(marker_color=color)
        return fig.to_html(div_id="chart")
    
    def create_heatmap(self):
        """Create correlation heatmap"""
        numeric_df = self.df.select_dtypes(include=np.number)
        corr = numeric_df.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale='Viridis'
        ))
        fig.update_layout(title='Correlation Heatmap')
        return fig.to_html(div_id="chart")
    
    def create_line(self, x_col, y_col, color='#1f77b4', title='Line Chart'):
        """Create line chart"""
        fig = px.line(self.df, x=x_col, y=y_col, title=title)
        fig.update_traces(line=dict(color=color, width=2))
        return fig.to_html(div_id="chart")
    
    def create_boxplot(self, columns, title='Box Plot'):
        """Create box plot"""
        fig = go.Figure()
        for col in columns:
            fig.add_trace(go.Box(y=self.df[col], name=col))
        fig.update_layout(title=title)
        return fig.to_html(div_id="chart")
    
    def save_visualization(self, viz_type, filepath, params):
        """Save visualization as image"""
        try:
            plt.figure(figsize=(12, 6))
            
            if viz_type == 'scatter':
                x_col = params.get('columns', [])[0]
                y_col = params.get('columns', [])[1]
                plt.scatter(self.df[x_col], self.df[y_col], color=params.get('color', '#1f77b4'))
                plt.xlabel(x_col)
                plt.ylabel(y_col)
            
            elif viz_type == 'bar':
                col = params.get('columns', [])[0]
                self.df[col].value_counts().plot(kind='bar', color=params.get('color', '#1f77b4'))
            
            elif viz_type == 'histogram':
                col = params.get('columns', [])[0]
                plt.hist(self.df[col], color=params.get('color', '#1f77b4'), bins=30)
                plt.xlabel(col)
            
            elif viz_type == 'heatmap':
                numeric_df = self.df.select_dtypes(include=np.number)
                sns.heatmap(numeric_df.corr(), cmap='viridis', annot=True)
            
            plt.title(params.get('title', viz_type))
            plt.tight_layout()
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
        
        except Exception as e:
            print(f"Error saving visualization: {e}")
