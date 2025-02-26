# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error 

# ------------------------------
# 3. DATA VISUALIZATION
# ------------------------------

def plot_sales_trends(file_path):
    df = pd.read_csv(file_path)
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='Year', y='Sales', data=df, marker='o')
    plt.title('Yearly Sales Trends')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()
    
    return df