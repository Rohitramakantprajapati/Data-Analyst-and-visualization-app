# DataPro Analyst - Advanced Data Analysis Platform

🔥 **One-liner:** Upload your dataset → Select task → Get insights & outputs — all in one local-hosted platform.

## Overview

DataPro Analyst is a powerful, user-friendly web application for end-to-end data analysis. Whether you're a beginner or a data professional, this platform helps you clean, analyze, visualize, and model your data with ease.

## Features

### 1. **Data Upload & Preview**
- Upload CSV or Excel files
- Instant data preview showing rows, columns, and structure
- Display data types and missing values count
- View first 10 rows in formatted table

### 2. **Data Cleaning**
- **Handle Missing Values**: Drop, Mean, Median, Forward Fill, Backward Fill
- **Remove Duplicates**: Eliminate duplicate rows
- **Handle Outliers**: Using IQR or Z-score methods
- **Normalize Data**: StandardScaler or MinMaxScaler normalization

### 3. **Exploratory Data Analysis (EDA)**
- **Summary Statistics**: Mean, Median, Std Dev, Min, Max, Quartiles
- **Correlations**: Correlation matrix between numeric variables
- **Distributions**: Value counts and distribution analysis
- **Visual insights** of data patterns

### 4. **Interactive Visualizations**
- **Scatter Plot**: XY scatter plots with color customization
- **Bar Chart**: Categorical data visualization
- **Histogram**: Distribution visualization
- **Line Chart**: Trend analysis
- **Box Plot**: Outlier and distribution detection
- **Correlation Heatmap**: Feature relationships
- **Color Customization**: Choose any color for your charts
- **Export**: Download visualizations as PNG images

### 5. **Machine Learning Models**
- **Regression**: Linear Regression & Random Forest
  - Model comparison with R² scores
  - RMSE and MSE metrics
- **Classification**: Random Forest Classifier
  - Accuracy score
  - Multi-class support
- **Clustering**: K-Means
  - Configurable number of clusters
  - Inertia and silhouette scoring

### 6. **Export Functionality**
- Download cleaned data as CSV
- Export visualizations as high-resolution images
- Save model results and metrics

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 500MB for installation + dependencies
- **OS**: Windows, macOS, or Linux
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

## Installation

### Step 1: Check Python Installation
```bash
python --version
```
If Python is not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies
Navigate to the DataProAnalyst folder and run:

**Windows:**
```bash
run.bat
```

**macOS/Linux:**
```bash
pip install -r requirements.txt
python app.py
```

### Step 3: Start the Application
The server will start automatically and listen on `http://localhost:5000`

### Step 4: Open the App
- **Option 1**: Open `launcher.html` in your browser
- **Option 2**: Manually navigate to `http://localhost:5000`

## How to Use

### 1. Upload Your Data
1. Click "Select CSV or Excel File" in the Upload Data section
2. Choose your CSV or Excel file
3. Click "Upload File"
4. Your data preview will appear automatically

### 2. Clean Your Data
1. Check the cleaning options you need:
   - Handle Missing Values
   - Remove Duplicates
   - Handle Outliers
   - Normalize Data
2. Click "Clean Data"
3. Review the cleaned data preview

### 3. Analyze Your Data
1. Click "Run EDA" to get summary statistics, correlations, and distributions
2. View insights about your dataset

### 4. Visualize Your Data
1. Select chart type (Scatter, Bar, Histogram, etc.)
2. Choose columns to visualize
3. Pick your favorite color
4. Add a title (optional)
5. Click "Generate Chart"
6. Customize and export as PNG

### 5. Build Models
1. Select task type: Regression, Classification, or Clustering
2. Choose your target column (for Regression/Classification)
3. Or set number of clusters (for Clustering)
4. Click "Build Model"
5. View model performance metrics

### 6. Export Results
- **Export Cleaned Data**: Download as CSV
- **Export Charts**: Download visualizations as PNG
- Clear all data and start fresh

## Project Structure

```
DataProAnalyst/
├── app.py                 # Flask backend application
├── data_processing.py     # Data processing modules
├── requirements.txt       # Python dependencies
├── run.bat               # Windows startup script
├── launcher.html         # Application launcher
├── README.md             # This file
├── templates/
│   └── index.html        # Main web application UI
├── static/               # Static assets (if needed)
├── uploads/              # Temporary file uploads
└── downloads/            # Downloaded files
```

## Technical Stack

### Backend
- **Flask**: Web framework for API endpoints
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning models
- **Matplotlib & Seaborn**: Visualization

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with gradients and animations
- **JavaScript (Vanilla)**: Interactivity
- **Plotly**: Interactive charts

## API Endpoints

### File Operations
- `POST /api/upload` - Upload CSV/Excel file
- `GET /api/data-preview` - Get data preview
- `POST /api/clear` - Clear all data

### Data Processing
- `POST /api/clean-data` - Clean data based on options
- `GET /api/columns` - Get available columns

### Analysis
- `POST /api/eda` - Run exploratory data analysis
- `POST /api/model` - Build machine learning model
- `POST /api/visualize` - Create visualization

### Export
- `GET /api/export-data` - Download cleaned data
- `POST /api/export-visualization` - Download chart

## Configuration

### Modify Server Port
Open `app.py` and change the port in the last line:
```python
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)  # Change port here
```

### Increase Upload File Size
In `app.py`, modify:
```python
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB
```

## Troubleshooting

### Port 5000 Already in Use
- Change the port in `app.py` to another number (e.g., 5001)
- Or kill the process using the port:
  ```bash
  # Windows
  netstat -ano | findstr :5000
  taskkill /PID <PID> /F
  
  # macOS/Linux
  lsof -i :5000
  kill -9 <PID>
  ```

### Missing Python Packages
```bash
pip install --upgrade -r requirements.txt
```

### CORS Errors
Ensure the Flask app is running and accessible at `http://localhost:5000`

### Large File Upload Issues
- Increase `MAX_CONTENT_LENGTH` in `app.py`
- Break large files into smaller chunks

## Usage Examples

### Example 1: Sales Data Analysis
1. Upload your sales data (CSV)
2. Clean: Handle missing values with mean
3. Analyze: Check correlations between price and quantity
4. Visualize: Create scatter plot of price vs sales
5. Model: Build regression model to predict sales
6. Export: Download cleaned data and visualization

### Example 2: Customer Segmentation
1. Upload customer data (Excel)
2. Clean: Remove duplicates, normalize features
3. Analyze: Get summary statistics
4. Model: K-Means clustering with 3 clusters
5. Visualize: Create heatmap of correlations
6. Export: Download customer segments

## Performance Tips

- **Large Datasets**: Clean data first to reduce size
- **Many Columns**: Select relevant columns for visualization
- **Complex Models**: Use sampling for exploratory analysis
- **Export Optimization**: Export data in batches if very large

## Limitations

- Maximum file size: 100MB (adjustable in config)
- Processing time increases with dataset size
- Some visualizations may slow down with 1M+ rows
- Browser memory may limit real-time operations

## Future Enhancements

- Multi-file upload and merge
- Advanced time series analysis
- Deep learning model support
- Real-time collaboration
- Database integration
- Advanced statistical tests
- Custom formula support

## Support & FAQ

**Q: How do I use this on a different machine?**
A: Copy the entire DataProAnalyst folder to the other machine and run `run.bat`

**Q: Can I access this from other devices?**
A: Change `localhost` to `0.0.0.0` in `app.py` and use your machine's IP address

**Q: Is my data stored anywhere?**
A: No, all data is temporary and processed locally. Files are deleted when you restart.

**Q: Can I use this offline?**
A: Yes! It runs completely offline on your localhost

## License

This project is provided as-is for educational and personal use.

## Contact & Support

For issues or feature requests, check the application logs for error messages.

---

**Happy Data Analyzing!** 🚀

Made with ❤️ for data enthusiasts
