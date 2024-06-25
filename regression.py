# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

# Load the iris dataset
data = load_iris()
iris_df = pd.DataFrame(data=data.data, columns=data.feature_names)

# Rename columns for easier access
iris_df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Define the features and the target
X = iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']]
y = iris_df['PetalWidthCm']

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Generate random inputs from the range of each feature
random_inputs = [
    np.random.uniform(X['SepalLengthCm'].min(), X['SepalLengthCm'].max()),
    np.random.uniform(X['SepalWidthCm'].min(), X['SepalWidthCm'].max()),
    np.random.uniform(X['PetalLengthCm'].min(), X['PetalLengthCm'].max())
]

# Predict the PetalWidthCm for the generated random inputs
prediction = model.predict([random_inputs])

# Print the random inputs and the prediction
print(f"Random inputs - SepalLengthCm: {random_inputs[0]:.2f}, SepalWidthCm: {random_inputs[1]:.2f}, PetalLengthCm: {random_inputs[2]:.2f}")
print(f"The predicted PetalWidthCm for these inputs is: {prediction[0]:.2f}")
