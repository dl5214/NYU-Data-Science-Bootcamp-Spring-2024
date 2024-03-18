# 3) Implement a custom function to categorize time of day into morning, afternoon, evening, and night,
# and create a new column in the DataFrame to store these categories. Use this new column to analyze
# pedestrian activity patterns throughout the day.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Load the dataset
    data_url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(data_url)

    # Convert the 'hour_beginning' column to datetime format
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    # Assuming 'hour_beginning' can be used to extract the hour
    df['hour'] = df['hour_beginning'].dt.hour

    def categorize_time_of_day(hour):
        if 5 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 21:
            return 'Evening'
        else:
            return 'Night'

    # Create the 'Time of Day' column using the categorize_time_of_day function
    df['Time of Day'] = df['hour'].apply(categorize_time_of_day)

    # First, ensure 'Time of Day' and 'Pedestrians' columns are present and correct
    print(df[['Time of Day', 'Pedestrians']].head())

    # Filter the DataFrame to include only the columns needed for the operation
    df_filtered = df[['Time of Day', 'Pedestrians']].copy()

    # Now, perform the grouping and summing operation on this filtered DataFrame
    time_of_day_counts = df_filtered.groupby('Time of Day')['Pedestrians'].sum()

    # Plotting the pedestrian activity patterns by time of day
    plt.figure(figsize=(10, 6))
    time_of_day_counts.plot(kind='bar')
    plt.title('Pedestrian Activity Patterns Throughout the Day')
    plt.xlabel('Time of Day')
    plt.ylabel('Total Pedestrian Count')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    main()