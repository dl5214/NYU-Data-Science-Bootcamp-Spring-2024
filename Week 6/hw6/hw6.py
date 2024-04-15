import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the CSV file into a DataFrame
csv_path = './employee.csv'
employee_df = pd.read_csv(csv_path)

# Preprocessing the data
# Convert categorical data to numeric using get_dummies
df_processed = pd.get_dummies(employee_df, columns=[
    'country', 'employment_status', 'job_title', 'education',
    'is_education_computer_related', 'certifications', 'is_manager'
], drop_first=True)

# Drop the 'timestamp' column as it is not needed for the model
df_processed.drop(['timestamp'], axis=1, inplace=True)

# Fill NaN values only for numeric columns
numeric_columns = df_processed.select_dtypes(include=[np.number]).columns
df_processed[numeric_columns] = df_processed[numeric_columns].fillna(df_processed.mean())

# Split the data into features and target variable
# 'id' and 'salary' columns are excluded as they are not predictive for the model
X = df_processed.drop(['id', 'salary'], axis=1)
y = df_processed['salary']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Predict the test set results
y_pred_linear = linear_reg.predict(X_test)

# Initialize and train the Ridge Regression model
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)
y_pred_ridge = ridge_reg.predict(X_test)

# Initialize and train the Lasso Regression model
lasso_reg = Lasso(alpha=1.0)
lasso_reg.fit(X_train, y_train)
y_pred_lasso = lasso_reg.predict(X_test)

# Compute evaluation metrics for all models
mae_linear = mean_absolute_error(y_test, y_pred_linear)
mse_linear = mean_squared_error(y_test, y_pred_linear)
rmse_linear = np.sqrt(mse_linear)

mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
rmse_ridge = np.sqrt(mse_ridge)

mae_lasso = mean_absolute_error(y_test, y_pred_lasso)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
rmse_lasso = np.sqrt(mse_lasso)

# Compile results
results = {
    "Linear Regression": {
        "Mean Absolute Error": mae_linear,
        "Mean Squared Error": mse_linear,
        "Root Mean Squared Error": rmse_linear
    },
    "Ridge Regression": {
        "Mean Absolute Error": mae_ridge,
        "Mean Squared Error": mse_ridge,
        "Root Mean Squared Error": rmse_ridge
    },
    "Lasso Regression": {
        "Mean Absolute Error": mae_lasso,
        "Mean Squared Error": mse_lasso,
        "Root Mean Squared Error": rmse_lasso
    }
}

# Display results
for model, metrics in results.items():
    print(model + ':')
    for metric, value in metrics.items():
        print(f' {metric}: {value:.2f}')
    print()
