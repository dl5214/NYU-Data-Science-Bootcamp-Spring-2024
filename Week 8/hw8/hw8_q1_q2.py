import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score


def main(column='Al'):
    # Load the dataset
    data = pd.read_csv('./glass.csv')

    # Display the first few rows of the dataset
    # print(data.head())

    # Define binary target: 1 if Type == 1, 0 otherwise
    data['Binary_Target'] = (data['Type'] == 1).astype(int)

    # Features and target
    X = data[[column]]
    y = data['Binary_Target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Normalize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Logistic regression model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Prediction probabilities
    probabilities = model.predict_proba(X_test_scaled)[:, 1]

    # Evaluate model at different thresholds
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for threshold in thresholds:
        predictions = (probabilities > threshold).astype(int)
        acc = accuracy_score(y_test, predictions)
        prec = precision_score(y_test, predictions)
        rec = recall_score(y_test, predictions)
        print(f'Threshold: {threshold:.1f}, Accuracy: {acc:.2f}, Precision: {prec:.2f}, Recall: {rec:.2f}')


if __name__ == '__main__':
    main(column='Al')  # change the column name for other columns in question2