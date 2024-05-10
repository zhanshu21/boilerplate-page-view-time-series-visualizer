import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=[0])

# Clean data
mask = (df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))
df = df[mask]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))

    ax.plot(df.index, df['value'], color='red', linewidth=3)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_hist = df.copy()
    df_hist['year'] = df.index.year
    df_hist['month'] = df.index.month

     # Group the DataFrame by year and month, 
    # and calculate the average page views for each group
    df_hist = df_hist.groupby(['year', 'month']).mean().reset_index()

    # Pivot the DataFrame to have years as rows and months as columns
    df_hist = df_hist.pivot(index='year', columns='month', values='value')

    # Define month names for the legend
    month_names =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # simpler way: using dataFrame.plot
    # Plotting
    ax = df_hist.plot(kind='bar', figsize=(15, 13))
    ax.legend(title='Months', labels=month_names)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views by Month')

    fig = ax.get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    
    month_names =["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, axes= plt.subplots(nrows=1, ncols=2, figsize=(28, 10))

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', 
                order=month_names, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
