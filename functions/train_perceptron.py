import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelEncoder


def train_perceptron(file_path):
    # Load the dataset from a CSV file
    data = pd.read_csv(file_path)

    # Encode the target labels ('positivo' as 1, 'negativo' as 0)
    label_encoder = LabelEncoder()
    data['resultado'] = label_encoder.fit_transform(data['resultado'])

    # Perform one-hot encoding for categorical features (columns 1-9)
    data = pd.get_dummies(data, columns=data.columns[:-1])

    # Split the dataset into features (X) and labels (y)
    X = data.iloc[:, :-1]
    y = data['resultado']

    # Initialize the Perceptron classifier
    perceptron_model = Perceptron(max_iter=1000)

    # Train the Perceptron on the entire dataset
    perceptron_model.fit(X, y)

    return perceptron_model



