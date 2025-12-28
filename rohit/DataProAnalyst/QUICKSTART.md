# DataPro Analyst - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Python (First Time Only)
- Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**
- Verify installation by opening Command Prompt and typing:
  ```
  python --version
  ```

### Step 2: Start the Server
1. Open the DataProAnalyst folder
2. **Double-click `run.bat`** (Windows)
3. Or run in Command Prompt:
   ```
   python app.py
   ```
4. Wait for message: "Running on http://localhost:5000"

### Step 3: Open the App
- **Option A**: Double-click `launcher.html` file
- **Option B**: Manually open in browser: `http://localhost:5000`

## 📊 Basic Workflow

```
Upload Data → Clean Data → Run Analysis → Create Visualization → Export Results
```

### Upload Your Data
1. Click "Select CSV or Excel File"
2. Choose your file
3. Click "Upload File"

### Clean Your Data
1. Check options (Handle Missing, Remove Duplicates, etc.)
2. Click "Clean Data"

### Analyze
1. Click "Run EDA" for statistics
2. Click "Visualize Data" for charts
3. Click "Build Model" for ML models

### Export
1. Click "Export Cleaned Data" to download CSV
2. Click "Export Chart" to download visualizations

## 🎯 Common Tasks

### Task: Analyze Sales Data
```
1. Upload sales.csv
2. Clean: Remove duplicates, handle missing values
3. EDA: View summary statistics
4. Visualize: Bar chart of sales by product
5. Model: Regression to predict future sales
6. Export: Download cleaned data
```

### Task: Customer Segmentation
```
1. Upload customers.xlsx
2. Clean: Normalize numeric columns
3. Analyze: Get correlations
4. Model: Clustering with 3 groups
5. Export: Download segments
```

### Task: Data Quality Check
```
1. Upload any_data.csv
2. Check: View missing values count
3. Clean: Handle all issues
4. Export: Download cleaned version
```

## ⚙️ Keyboard Shortcuts & Tips

- Press Enter in file input to upload
- Hold Ctrl/Cmd to select multiple columns
- Right-click on chart to download
- Scroll in sidebar for more options

## 🛠️ Troubleshooting

### "Server not running"
- Make sure run.bat is executing
- Check if Python is installed: `python --version`

### "Port 5000 in use"
- Close other applications using port 5000
- Or change port in app.py (line: `port=5000`)

### "File upload fails"
- Check file format (CSV or Excel only)
- File size under 100MB
- No special characters in filename

### "Visualization not showing"
- Select at least 1 column
- Check data has numeric or categorical values
- Refresh browser (F5)

## 📁 File Organization

```
DataProAnalyst/
├── launcher.html          👈 Double-click to open app
├── run.bat               👈 Double-click to start server
├── README.md             📖 Full documentation
├── QUICKSTART.md         📋 This file
├── app.py                ⚙️ Backend code
├── requirements.txt      📦 Dependencies
└── data_processing.py    🔧 Data tools
```

## 🎨 Customization

### Change App Colors
Edit templates/index.html, find:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
Replace with your colors.

### Change Default Port
Edit app.py, find:
```python
app.run(debug=True, host='localhost', port=5000)
```
Change port number.

## 📚 Learn More

- Full documentation: [README.md](README.md)
- Example datasets: Create sample CSV files
- Python docs: [python.org/docs](https://docs.python.org/)

## 💡 Pro Tips

1. **Large Files**: Clean data before complex analysis
2. **Visualization**: Use different colors to compare charts
3. **Models**: Start with simple models, then try complex ones
4. **Export**: Download results regularly for backup
5. **Columns**: Select relevant columns to speed up processing

## 🔗 Useful Links

- Python: https://www.python.org/downloads/
- Pandas Docs: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/
- Flask: https://flask.palletsprojects.com/

## ❓ FAQ

**Q: Do I need internet?**
A: No! Everything runs locally on your computer.

**Q: Is my data secure?**
A: Yes! Data never leaves your computer. It's only stored in RAM during the session.

**Q: Can I share with others?**
A: Yes! Share the entire DataProAnalyst folder. They just need Python installed.

**Q: How do I update the app?**
A: Download the latest version and overwrite files (keep your data in uploads/).

---

🎉 **You're all set!** Start analyzing your data now.
