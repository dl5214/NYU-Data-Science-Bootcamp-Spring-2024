# 2) Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different
# weather conditions influence pedestrian activity in that year. Sort the pedestrian count data
# by weather summary to identify any correlations( with a correlation matrix) between weather patterns
# and pedestrian counts for the selected year.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def main():
    # Load the dataset
    data_url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(data_url)

    # Convert the 'hour_beginning' column to datetime format
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    # Correctly referencing the 'weather_summary' column
    df['year'] = df['hour_beginning'].dt.year
    df_2019_brooklyn_bridge = df[(df['year'] == 2019) & (df['location'].str.contains('Brooklyn Bridge'))]

    # Assuming df_2019_brooklyn_bridge is correctly filtered to only include data for 2019 and the Brooklyn Bridge
    # Group by 'weather_summary' and explicitly sum only the 'Pedestrians' column, then sort the results
    weather_counts = df_2019_brooklyn_bridge.groupby('weather_summary')['Pedestrians'].sum().sort_values()

    # Continue with the correlation matrix analysis
    # Ensure that the DataFrame used in the correlation matrix only contains numeric columns
    numeric_df = df_2019_brooklyn_bridge.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Weather Conditions and Pedestrian Counts')
    plt.show()


if __name__ == '__main__':
    main()