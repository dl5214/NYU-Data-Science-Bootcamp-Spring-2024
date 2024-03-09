# 1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    filtered_df = df[['Manufacturer','Model','Type']].iloc[::20]
    print(filtered_df)


if __name__ == '__main__':
    main()