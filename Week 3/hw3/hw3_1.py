# 1)Filter the data to include only weekdays (Monday to Friday) and plot a line graph
# showing the pedestrian counts for each day of the week.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Load the dataset
    data_url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(data_url)

    # print(df.columns)
    print(df['hour_beginning'].head())  # Print a sample to inspect the format

    # Convert the 'hour_beginning' column to datetime format
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    # Filter out weekends
    data_weekdays = df[df['hour_beginning'].dt.dayofweek < 5]

    # Group by day of the week and sum ONLY the 'Pedestrians' column
    weekday_counts = data_weekdays.groupby(data_weekdays['hour_beginning'].dt.day_name())['Pedestrians'].sum()

    # Order the days
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekday_counts = weekday_counts.reindex(ordered_days)

    # Plotting
    plt.figure(figsize=(10, 6))
    weekday_counts.plot(kind='line')
    plt.title('Pedestrian Counts by Weekday')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Pedestrian Count')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()