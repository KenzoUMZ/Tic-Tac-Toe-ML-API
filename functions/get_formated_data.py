import pandas as pd

def getFormatedData():
    data = pd.read_csv('tic_tac_toe.csv')

    data[:] = data[:].replace('x', '+1')
    data[:] = data[:].replace('b', '0')
    data[:] = data[:].replace('o', '-1')
    data['resultado'] = data['resultado'].replace('positivo', '+1')
    data['resultado'] = data['resultado'].replace('negativo', '-1')

    positiveTests = data[:96]
    negativeTests = data[-96:]
    toConcatTests = [positiveTests, negativeTests]
    tests = pd.concat(toConcatTests)
    testsSamples = tests.iloc[:, :9]
    
    data = data.drop(data.index[:96])
    data = data.drop(data.index[-96:])
    samples = data.iloc[:, :9]
    targets = data.iloc[:, 9]

    return [testsSamples, samples, targets]