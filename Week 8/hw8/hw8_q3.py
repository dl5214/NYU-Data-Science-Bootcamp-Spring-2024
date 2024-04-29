import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def main():
    # Load the dataset
    data = pd.read_csv('./glass.csv')

    # Define binary target: 1 if Type == 1, 0 otherwise
    data['Binary_Target'] = (data['Type'] == 1).astype(int)

    # Preparing the full features set excluding the 'Type' and 'Binary_Target' columns
    X_full = data.drop(columns=['Type', 'Binary_Target'])
    y_full = data['Binary_Target']

    # Splitting the dataset
    X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_full, y_full, test_size=0.3, random_state=42)

    # Creating a logistic regression pipeline with normalization
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    pipeline.fit(X_train_full, y_train_full)

    # Evaluating the model
    score = pipeline.score(X_test_full, y_test_full)
    print(f'Accuracy of the model on all features: {score:.2f}')


if __name__ == '__main__':
    main()