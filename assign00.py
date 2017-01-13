import numpy
import random
from math import floor
from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
iris = datasets.load_iris()

# Show the data (the attributes of each instance)
print(iris.data)

# Show the target values (in numeric format) of each instance
print(iris.target)

# Show the actual target names that correspond to each number
print(iris.target_names)

data_train, data_test, target_train, target_test = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(100, 500))

class HardCoded:
    def predict(self, data):
        return 0
    def fit(self, row):
        return

def testAccuracy(classifier, testData, testTarget):
    numRight = 0
    numWrong = 0
    answer = 0
    target = 0
    for i in range(0, len(testData)):
        answer = classifier.predict(testData[i])
        target = testTarget[i]
        if answer == target:
            numRight += 1
        else:
            numWrong += 1
    return numRight / (numRight + numWrong)

classifer = HardCoded()

print(testAccuracy(classifer, data_test, target_test))