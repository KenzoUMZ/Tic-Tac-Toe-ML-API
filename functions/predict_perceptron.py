
def predict_with_perceptron(model, input_data):
    # Make predictions using the trained Perceptron model
    # Input_data should be a DataFrame with the same format as the training data
    predictions = model.predict(input_data)

    return predictions
