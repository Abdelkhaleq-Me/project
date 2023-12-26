import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
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

#split the data into features "X" and target "Y"
X = data.iloc[:,1:]
Y = data['Energie']
#split the data into training data and test data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)


poly = PolynomialFeatures(degree=3, include_bias=False)
poly_features = poly.fit_transform(X)
print(poly_features)
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, Y)
y_predicted = poly_reg_model.predict(poly_features)
R_score = r2_score(Y, y_predicted)
print(f"R_scored: {R_score}")
plt.figure(figsize=(10,4))
plt.title("PolynomialREgression",size=6)
plt.scatter(X,Y)
plt.plot(X,y_predicted,c="red")
plt.xlabel('x')
plt.ylabel("y")
plt.show()

