# sea_level_predictor.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Line of best fit for all data
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(years_all, intercept_all + slope_all * years_all, 'r', label='Fit All Years')

    # Line of best fit from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'green', label='Fit 2000+')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.tight_layout()
    
    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt
