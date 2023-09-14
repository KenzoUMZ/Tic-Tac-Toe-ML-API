from sklearn.linear_model import Perceptron

def train_model(samples, targets):
    model = Perceptron()
    model.fit(X=samples, y=targets)
    return model
