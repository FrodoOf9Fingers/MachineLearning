from sklearn import datasets
from experimentShell import ExperimentShell
from KNNClassifier import kNNClassifier
from usefulFunctions import loadCSV
import random
from sklearn.cross_validation import train_test_split as tts

def lowHighConvert(x):
    return {
        'low': 1,
        'med': 2,
        'high': 3,
        'vhigh': 4,
    }.get(x, 0)    # default to 0

def carsC2(x):
    return {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5more': 5
    }.get(x, 0)    # default to 0

def carsC3(x):
    return {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        'more': 5
    }.get(x, 0)    # default to 0

def carsC4(x):
    return {
        'big': 3,
        'med': 2,
        'small': 1,
    }.get(x, 0)    # default to 0

def carsTarget(x):
    return {
        'unacc': 1,
        'acc': 2,
        'good': 3,
        'vgood': 4
    }.get(x, 0)    # default to 0

def fitCarData(rawData):
    data = [[0 for y in range (0, len(rawData[0]))] for x in range(0, len(rawData))]
    target = [0 for x in range(0, len(rawData))]
    for i in range(0, len(rawData)):
        data[i][0] = lowHighConvert(rawData[i][0])
        data[i][1] = lowHighConvert(rawData[i][1])
        data[i][2] = carsC2(rawData[i][2])
        data[i][3] = carsC3(rawData[i][3])
        data[i][4] = carsC4(rawData[i][4])
        data[i][5] = lowHighConvert(rawData[i][5])
        target[i] = carsTarget(rawData[i][6])
    return data, target


iris = datasets.load_iris()
classifier = kNNClassifier()
classifier.k = 1
XPShell = ExperimentShell()
XPShell.setClassifier(classifier)

XPShell.m_data_test, \
XPShell.m_data_train, \
XPShell.m_target_test, \
XPShell.m_target_train = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(100, 500))

print ("Iris test data with kNN")
print(XPShell.test())

rawCarData = loadCSV('cars.csv')
carData, carTarget = fitCarData(rawCarData)

XPShell.m_data_test, \
XPShell.m_data_train, \
XPShell.m_target_test, \
XPShell.m_target_train = tts(carData, carTarget, train_size=.7, random_state=random.randint(100, 500))

print ("Car test data with kNN")
print(XPShell.test())
