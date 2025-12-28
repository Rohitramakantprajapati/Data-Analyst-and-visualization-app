# 🚀 DataPro Analyst - Complete Installation & Usage Guide

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Starting the Application](#starting-the-application)
4. [Using the Application](#using-the-application)
5. [Features Overview](#features-overview)
6. [Troubleshooting](#troubleshooting)
7. [Sample Datasets](#sample-datasets)

---

## System Requirements

### Minimum Requirements
- **Python**: 3.8 or newer
- **RAM**: 4GB
- **Storage**: 500MB
- **OS**: Windows 10+, macOS 10.14+, or Linux

### Recommended Setup
- **Python**: 3.10+
- **RAM**: 8GB or more
- **SSD**: For faster file operations
- **Modern Browser**: Chrome, Firefox, Safari, or Edge

---

## Installation

### ✅ Step 1: Install Python

#### Windows
1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.10+ installer
3. Run installer and **CHECK** "Add Python to PATH"
4. Complete installation
5. Verify in Command Prompt:
   ```cmd
   python --version
   ```

#### macOS
```bash
brew install python3
python3 --version
```

#### Linux
```bash
sudo apt-get install python3.10
python3 --version
```

### ✅ Step 2: Navigate to Project Folder

#### Windows (Command Prompt)
```cmd
cd C:\Users\YourName\OneDrive\Desktop\rohit\DataProAnalyst
```

#### macOS/Linux (Terminal)
```bash
cd ~/Desktop/DataProAnalyst
```

### ✅ Step 3: Install Dependencies

#### Automatic (Windows)
```cmd
run.bat
```

#### Manual Installation
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**What gets installed:**
- Flask - Web server
- Pandas - Data manipulation
- NumPy - Numerical computing
- Scikit-learn - Machine learning
- Plotly - Interactive charts
- Matplotlib & Seaborn - Visualization
- OpenPyXL - Excel support

### ✅ Step 4: Verify Installation

Check if all packages installed correctly:
```bash
pip list
```

You should see:
- flask
- pandas
- numpy
- scikit-learn
- plotly
- matplotlib
- seaborn

---

## Starting the Application

### 🎯 Option 1: Windows Batch File (Easiest)
1. Open the `DataProAnalyst` folder
2. **Double-click** `run.bat`
3. Wait for: `"Running on http://localhost:5000"`
4. Batch file automatically opens your browser

### 🎯 Option 2: Command Prompt/Terminal
```bash
python app.py
```

Expected output:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://localhost:5000
```

### 🎯 Option 3: Open Launcher
1. Double-click `launcher.html`
2. Click "🚀 Start Application" button
3. App opens automatically

---

## Using the Application

### Complete Workflow

```
┌─────────────────────────────────────────────────────────┐
│           DataPro Analyst Workflow                      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
                  [1] UPLOAD DATA
        (CSV/Excel files, Preview)
                          │
                          ▼
                  [2] CLEAN DATA
    (Missing values, Duplicates, Outliers)
                          │
                          ▼
                  [3] ANALYZE DATA
        (Statistics, Correlations, EDA)
                          │
                          ▼
            [4] VISUALIZE & MODEL
    (Charts with colors, ML Models)
                          │
                          ▼
                  [5] EXPORT RESULTS
        (Download CSV, Images, Reports)
```

### Step-by-Step Usage

#### **Phase 1: Data Upload (2 minutes)**

1. **Locate your file**
   - Must be CSV or Excel (.xlsx, .xls)
   - Max size: 100MB
   - Example: `sales_data.csv`

2. **Click "Select CSV or Excel File"**
   - File dialog opens
   - Choose your data file
   - Click Open

3. **Click "📤 Upload File"**
   - File uploads to server
   - Preview appears automatically
   - Check data preview table

4. **Verify preview shows:**
   - Row count ✓
   - Column count ✓
   - Missing values ✓
   - Data types ✓
   - First 10 rows ✓

#### **Phase 2: Data Cleaning (5 minutes)**

1. **Select cleaning operations**
   - ☑ Handle Missing Values (choose method)
   - ☑ Remove Duplicates
   - ☑ Handle Outliers
   - ☑ Normalize Data

2. **Choose missing value method:**
   - **Drop**: Remove rows with missing values
   - **Mean**: Replace with average
   - **Median**: Replace with middle value
   - **Forward Fill**: Use previous value

3. **Click "🧹 Clean Data"**
   - Processing runs automatically
   - Preview updates with cleaned data
   - Status message confirms completion

4. **Review cleaned data**
   - Check missing values reduced
   - Verify row count (if using drop method)
   - Ensure data quality improved

#### **Phase 3: Exploratory Data Analysis (3 minutes)**

1. **Click "📊 Run EDA"**
   - Analysis runs in background
   - Results display automatically

2. **Review statistics:**
   - Mean, Median, Std Dev
   - Min/Max values
   - Quartile ranges

3. **Check correlations:**
   - Relationships between columns
   - Identify key factors

4. **Explore distributions:**
   - Value frequencies
   - Category counts
   - Pattern identification

#### **Phase 4: Data Visualization (5 minutes)**

1. **Choose visualization type:**
   - 📊 Scatter Plot (2 numeric columns)
   - 📈 Line Chart (trends over time)
   - 📊 Bar Chart (categories)
   - 📊 Histogram (distributions)
   - 📦 Box Plot (outliers/spread)
   - 🔥 Heatmap (correlations)

2. **Configure visualization:**
   - Select columns to plot
   - Choose color (color picker or RGB)
   - Enter custom title
   - Click "🎨 Generate Chart"

3. **Interact with chart:**
   - Hover for details
   - Zoom by clicking + dragging
   - Pan by holding shift
   - Download PNG via menu

4. **Export visualization:**
   - Click "💾 Export Chart"
   - Saves as high-quality PNG
   - Goes to downloads folder

#### **Phase 5: Machine Learning Models (5 minutes)**

1. **Choose model type:**
   - 🔢 **Regression**: Predict continuous values
   - 🎯 **Classification**: Predict categories
   - 🔀 **Clustering**: Group similar data

2. **For Regression/Classification:**
   - Select target column (what to predict)
   - Click "🚀 Build Model"
   - View model performance:
     - R² Score
     - Accuracy
     - RMSE (error metric)

3. **For Clustering:**
   - Set number of clusters (2-10)
   - Click "🚀 Build Model"
   - View cluster metrics:
     - Inertia
     - Silhouette score

4. **Interpret results:**
   - Higher R² = better fit (0-1)
   - Higher Accuracy = better predictions (0-100%)
   - Compare multiple models

#### **Phase 6: Export & Save (2 minutes)**

1. **Export cleaned data:**
   - Click "💾 Export Cleaned Data"
   - Downloads as CSV file
   - Ready for use elsewhere

2. **Export visualizations:**
   - From chart menu: Download as PNG
   - High resolution (300 DPI)
   - Use in reports/presentations

3. **Save multiple outputs:**
   - Export at different stages
   - Each export gets unique timestamp
   - Keep backups of results

---

## Features Overview

### 🆙 Upload Capabilities
- **Formats**: CSV, Excel (.xlsx, .xls)
- **Size**: Up to 100MB
- **Preview**: Instant data preview
- **Validation**: File type checking

### 🧹 Data Cleaning Tools

| Feature | Options | Use Case |
|---------|---------|----------|
| Missing Values | Drop, Mean, Median, Forward/Backward Fill | Handle incomplete data |
| Duplicates | Remove entire duplicate rows | Clean data quality |
| Outliers | IQR or Z-score method | Remove anomalies |
| Normalization | Standard or MinMax scaling | Prepare for ML |

### 📊 Analysis Features

| Feature | Description |
|---------|-------------|
| Summary Stats | Mean, Median, Std, Min, Max, Quartiles |
| Correlations | Identify relationships between variables |
| Distributions | Value frequencies and patterns |
| Data Insight | Quick statistics per column |

### 📈 Visualization Options

| Chart Type | Best For | Example |
|-----------|----------|---------|
| Scatter | Relationship between 2 variables | Price vs Quantity |
| Line | Trends over time | Sales over months |
| Bar | Category comparisons | Sales by product |
| Histogram | Distribution visualization | Age distribution |
| Box Plot | Outlier detection | Income by region |
| Heatmap | Correlation matrix | Feature relationships |

**Color Customization:**
- Choose from color picker
- 16 million color options
- Real-time preview

### 🤖 Machine Learning Models

#### Regression (Predict Numbers)
- **Linear Regression**: Simple, interpretable
- **Random Forest**: Better accuracy, handles non-linearity
- Metrics: R², RMSE, MSE

#### Classification (Predict Categories)
- **Random Forest Classifier**: Handles multiple classes
- Metrics: Accuracy, Precision, Recall

#### Clustering (Group Data)
- **K-Means**: Unsupervised grouping
- Configurable: 2-10 clusters
- Metrics: Inertia, Silhouette Score

### 💾 Export Options
- **Data**: CSV format (all rows/columns)
- **Visualizations**: PNG format (high quality)
- **Models**: Metrics and performance data
- **Timestamps**: Unique file naming

---

## Troubleshooting

### Common Issues & Solutions

#### ❌ "Server is not running"
**Problem**: Port 5000 not responding

**Solution**:
```bash
# Make sure app.py is running
python app.py

# Check if port is in use
netstat -ano | findstr :5000

# Use different port in app.py
# Change: port=5000 to port=5001
```

#### ❌ "Module not found" Error
**Problem**: Python packages not installed

**Solution**:
```bash
# Reinstall all packages
pip install --upgrade -r requirements.txt

# Or install individually
pip install flask pandas numpy scikit-learn plotly
```

#### ❌ "File upload fails"
**Problem**: File too large or invalid format

**Solutions**:
- Ensure file is CSV or Excel
- File size < 100MB
- No special characters in filename
- File not corrupted

#### ❌ "Visualization not displaying"
**Problem**: Chart won't render

**Solutions**:
- Select at least one column
- Ensure column has valid data
- Refresh page (F5)
- Check browser console (F12) for errors

#### ❌ "Python not recognized"
**Problem**: PATH not set correctly

**Solution**:
- Reinstall Python with "Add to PATH" checked
- Or manually add Python to PATH:
  - Windows: Set environment variable
  - macOS/Linux: Add to .bash_profile

#### ❌ "Port already in use"
**Problem**: Another app using port 5000

**Solutions**:
```bash
# Kill process using port
# Windows
taskkill /PID <process_id> /F

# macOS/Linux
kill -9 <process_id>

# Or change port in app.py
app.run(port=5001)
```

### Performance Tips

- **Large Files**: Clean data first to reduce size
- **Many Columns**: Select relevant columns only
- **Slow Visualizations**: Use smaller datasets for real-time
- **Memory Issues**: Process in batches
- **Browser Slow**: Clear cache and restart

---

## Sample Datasets

### Generate Sample Data

1. **Run generator script:**
   ```bash
   python generate_sample_data.py
   ```

2. **Creates 4 sample datasets:**
   - `sales_data.csv` - Product sales with regions
   - `customer_data.csv` - Customer demographics
   - `health_data.csv` - Health metrics
   - `education_data.csv` - Student performance

### Sample Workflow Examples

#### Example 1: Sales Analysis
```
1. Upload: sales_data.csv
2. Clean: Remove duplicates, handle missing satisfaction
3. Analyze: Check sales by product
4. Visualize: Bar chart of units by product
5. Model: Predict sales using regression
6. Export: Download cleaned sales data
```

#### Example 2: Customer Segmentation
```
1. Upload: customer_data.csv
2. Clean: Normalize income and spending
3. Analyze: Get spending statistics
4. Model: K-means clustering with 4 groups
5. Visualize: Heatmap of correlations
6. Export: Download customer segments
```

#### Example 3: Health Data Analysis
```
1. Upload: health_data.csv
2. Clean: Handle missing sleep hours
3. Analyze: Get health metrics statistics
4. Visualize: Scatter plot of weight vs cholesterol
5. Model: Predict health metrics
6. Export: Download analysis results
```

---

## Next Steps

### Getting More from DataPro Analyst

1. **Try Different Datasets**
   - Use your own data
   - Test with various file sizes
   - Try different analysis scenarios

2. **Explore All Features**
   - Try each visualization type
   - Build different model types
   - Experiment with colors

3. **Learn Data Analysis**
   - Study the generated statistics
   - Understand correlations
   - Interpret model metrics

4. **Share Results**
   - Export visualizations
   - Share analysis reports
   - Create presentations

### Advanced Usage

- Modify source code for custom analysis
- Integrate with other tools
- Process larger datasets
- Add custom models

---

## Support & FAQ

**Q: Is my data private?**
A: Yes! All data stays on your computer. Nothing is uploaded to external servers.

**Q: Can I process 10GB+ files?**
A: Large files will be slow. Recommended: clean/sample first.

**Q: How do I change the port?**
A: Edit `app.py`, change `port=5000` to your port number.

**Q: Can I use this offline?**
A: Yes! No internet required. Runs entirely locally.

**Q: How do I add custom columns?**
A: Prepare data beforehand and upload with new columns.

**Q: Can multiple people use at once?**
A: Change `localhost` to `0.0.0.0` in app.py for network access.

---

## Quick Reference

### Keyboard Shortcuts
- `Ctrl/Cmd + S`: Save results
- `F5`: Refresh page
- `F12`: Developer console
- `Escape`: Close dialogs

### File Locations
- App folder: `DataProAnalyst/`
- Uploads: `DataProAnalyst/uploads/`
- Downloads: `DataProAnalyst/downloads/`
- Source code: `DataProAnalyst/*.py`

### Port Reference
- Default: `http://localhost:5000`
- If changed: `http://localhost:YOUR_PORT`

---

**Happy Analyzing! 🚀**

For more help, check README.md or QUICKSTART.md
