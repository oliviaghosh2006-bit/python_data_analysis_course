# time_series_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data: remove top 2.5% and bottom 2.5% of page views
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_quantile) & (df['value'] <= upper_quantile)]

def draw_line_plot():
    # Draw line plot of daily page views
    data = df.copy()
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.tight_layout()
    plt.savefig("line_plot.png")
    return plt

def draw_bar_plot():
    # Draw bar plot of average monthly page views per year
    data = df.copy()
    data['year'] = data.index.year
    data['month'] = data.index.month_name()

    # Group by year and month
    df_bar = data.groupby(['year', 'month'])['value'].mean().unstack()

    # Ensure months are in calendar order
    months_order = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    df_bar = df_bar[months_order]

    # Plot
    df_bar.plot(kind='bar', figsize=(12,6))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.tight_layout()
    plt.savefig("bar_plot.png")
    return plt

def draw_box_plot():
    # Prepare data for box plots
    data = df.copy().reset_index()
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')  # abbreviated month
    data['month_num'] = data['date'].dt.month

    # Sort by month number for correct order
    data = data.sort_values('month_num')

    # Draw box plots (year-wise and month-wise)
    fig, axes = plt.subplots(1, 2, figsize=(15,6))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.savefig("box_plot.png")
    return plt
