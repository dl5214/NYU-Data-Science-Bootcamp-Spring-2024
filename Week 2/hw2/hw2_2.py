# 2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    df.to_csv('./hw2_2_original.csv', index=False)
    df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
    df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
    df.to_csv('./hw2_2_modified.csv', index=False)


if __name__ == '__main__':
    main()