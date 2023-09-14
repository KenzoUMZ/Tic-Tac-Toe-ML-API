import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelEncoder


def train_model(samples, targets):
    model = Perceptron()
    model.fit(X=samples, y=targets)
    return model
