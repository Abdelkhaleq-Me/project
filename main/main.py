import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , mean_squared_error
data = pd.read_csv("/home/wahid/Electricity_Consumption_Prediction_System/main/Electricity_consumption_history.csv")

#delet the "typedejour" column because ae do not need it
data = data.iloc[:,[0,2,3]]

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Sort data by date
data = data.sort_values(by='Date')

# Extract date features
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# remove the first column 'Date'
data = data.iloc[:,1:]

# Split the data into features "X" and target "Y"
X = data.iloc[:,1:]
Y = data['Energie']

# Polynomial Regression
poly = PolynomialFeatures(degree=7, include_bias=False)
poly_features = poly.fit_transform(X)

#split the data into training data and test data
x_train, x_test, y_train, y_test = train_test_split(poly_features, Y, test_size=0.2,random_state=100)

# Train the polynomial regression model
poly_reg_model = LinearRegression()
poly_reg_model.fit(x_train, y_train)

# Prediction
y_predicted = poly_reg_model.predict(x_test)

# Model Evaluation using R squared and cost function(mean squared error)
R2_score = r2_score(y_test, y_predicted)
mse = mean_squared_error(y_test,y_predicted)
print(f"R2 score: {R2_score}")
print(f"mean squared error: {mse}")

