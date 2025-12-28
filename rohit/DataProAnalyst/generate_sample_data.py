"""
Sample Data Generator for DataPro Analyst
This script generates sample datasets for testing the application
"""

import pandas as pd
import numpy as np
import os

def generate_sales_data():
    """Generate sample sales dataset"""
    np.random.seed(42)
    n_samples = 200
    
    data = {
        'Date': pd.date_range('2023-01-01', periods=n_samples, freq='D'),
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'], n_samples),
        'Units_Sold': np.random.randint(1, 100, n_samples),
        'Price_per_Unit': np.random.uniform(50, 2000, n_samples),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'Customer_Age': np.random.randint(18, 80, n_samples),
        'Satisfaction': np.random.uniform(1, 5, n_samples),
    }
    
    data['Total_Sales'] = data['Units_Sold'] * data['Price_per_Unit']
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    missing_indices = np.random.choice(n_samples, 15, replace=False)
    df.loc[missing_indices, 'Satisfaction'] = np.nan
    
    return df

def generate_customer_data():
    """Generate sample customer dataset"""
    np.random.seed(42)
    n_samples = 300
    
    data = {
        'Customer_ID': range(1001, 1001 + n_samples),
        'Age': np.random.randint(18, 75, n_samples),
        'Income': np.random.randint(30000, 150000, n_samples),
        'Spending': np.random.randint(100, 5000, n_samples),
        'Years_Customer': np.random.randint(0, 20, n_samples),
        'Purchases': np.random.randint(1, 50, n_samples),
        'Gender': np.random.choice(['M', 'F'], n_samples),
        'Location': np.random.choice(['Urban', 'Rural', 'Suburban'], n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    missing_indices = np.random.choice(n_samples, 20, replace=False)
    df.loc[missing_indices, 'Income'] = np.nan
    
    return df

def generate_health_data():
    """Generate sample health dataset"""
    np.random.seed(42)
    n_samples = 250
    
    data = {
        'Patient_ID': range(1, n_samples + 1),
        'Age': np.random.randint(20, 80, n_samples),
        'Height_cm': np.random.normal(170, 15, n_samples),
        'Weight_kg': np.random.normal(75, 20, n_samples),
        'Blood_Pressure_Systolic': np.random.normal(120, 15, n_samples),
        'Blood_Pressure_Diastolic': np.random.normal(80, 10, n_samples),
        'Cholesterol': np.random.normal(200, 50, n_samples),
        'Exercise_Hours_Per_Week': np.random.uniform(0, 15, n_samples),
        'Sleep_Hours': np.random.uniform(4, 10, n_samples),
        'Stress_Level': np.random.choice([1, 2, 3, 4, 5], n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    missing_indices = np.random.choice(n_samples, 25, replace=False)
    df.loc[missing_indices, 'Sleep_Hours'] = np.nan
    
    return df

def generate_education_data():
    """Generate sample education dataset"""
    np.random.seed(42)
    n_samples = 400
    
    data = {
        'Student_ID': range(1, n_samples + 1),
        'Age': np.random.randint(18, 25, n_samples),
        'Math_Score': np.random.normal(75, 15, n_samples),
        'English_Score': np.random.normal(70, 18, n_samples),
        'Science_Score': np.random.normal(73, 16, n_samples),
        'Attendance_Percent': np.random.uniform(60, 100, n_samples),
        'Study_Hours_Per_Week': np.random.uniform(5, 40, n_samples),
        'Extracurricular': np.random.choice(['Yes', 'No'], n_samples),
        'GPA': np.random.uniform(2.0, 4.0, n_samples),
        'Parent_Education': np.random.choice(['HS', 'Bachelor', 'Master', 'PhD'], n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    missing_indices = np.random.choice(n_samples, 30, replace=False)
    df.loc[missing_indices, 'GPA'] = np.nan
    
    return df

def main():
    """Generate and save all sample datasets"""
    
    # Create samples directory
    samples_dir = 'sample_data'
    os.makedirs(samples_dir, exist_ok=True)
    
    print("Generating sample datasets...")
    
    # Sales data
    df_sales = generate_sales_data()
    df_sales.to_csv(f'{samples_dir}/sales_data.csv', index=False)
    print("✓ Created: sales_data.csv (200 records)")
    
    # Customer data
    df_customers = generate_customer_data()
    df_customers.to_csv(f'{samples_dir}/customer_data.csv', index=False)
    print("✓ Created: customer_data.csv (300 records)")
    
    # Health data
    df_health = generate_health_data()
    df_health.to_csv(f'{samples_dir}/health_data.csv', index=False)
    print("✓ Created: health_data.csv (250 records)")
    
    # Education data
    df_education = generate_education_data()
    df_education.to_csv(f'{samples_dir}/education_data.csv', index=False)
    print("✓ Created: education_data.csv (400 records)")
    
    # Also create Excel versions
    try:
        df_sales.to_excel(f'{samples_dir}/sales_data.xlsx', index=False)
        df_customers.to_excel(f'{samples_dir}/customer_data.xlsx', index=False)
        print("✓ Created: Excel versions of datasets")
    except Exception as e:
        print(f"⚠ Could not create Excel files: {e}")
    
    print(f"\n✅ All sample datasets created in '{samples_dir}/' folder!")
    print("\nDataset Descriptions:")
    print("=" * 50)
    print("1. sales_data.csv - Sales transactions with products")
    print("2. customer_data.csv - Customer demographics & spending")
    print("3. health_data.csv - Health metrics and vitals")
    print("4. education_data.csv - Student academic performance")
    print("\nUse these files to test DataPro Analyst features!")

if __name__ == '__main__':
    main()
