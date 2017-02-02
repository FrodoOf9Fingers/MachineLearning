from sklearn import datasets
from experimentShell import ExperimentShell
from ID3Classifier import iD3Classifier
from carData import CarData
from lensesData import LensesData
from votingData import VotingData
import random
from sklearn.cross_validation import train_test_split as tts
from sklearn import tree

iris = datasets.load_iris()
classifier = iD3Classifier()
clf = tree.DecisionTreeRegressor()
XPShell = ExperimentShell()
XPShell.setClassifier(classifier)
XPShell.m_comparator = clf

#XPShell.m_data_test, \
#XPShell.m_data_train, \
#XPShell.m_target_test, \
#XPShell.m_target_train = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(100, 500))

#print ("Iris test data with ID3")
#print(XPShell.test())
#Voting Data!
dataObj = VotingData()
dataObj.loadData()
data = dataObj.rawData
target = dataObj.rawTarget


avgPerformance = 0
avgComparator = 0
successfulIterations = 0
for i in range(0, 10):
    noError = True
    dtest, dtrain, ttest, ttrain = tts(data, target, train_size=.7, random_state=random.randint(100, 500))
    for item in dtrain:
        if len(item) != len(dtrain[0]):
            #print("The Heck???") tts seems to carry state from iteration to iteration
            noError = False
            break
    if noError == True:
        XPShell.m_data_test = dtest
        XPShell.m_data_train = dtrain
        XPShell.m_target_test = ttest
        XPShell.m_target_train = ttrain
        avgPerformance += XPShell.test()
        avgComparator += XPShell.testComparator()
        successfulIterations += 1

avgPerformance /= successfulIterations
avgComparator /= successfulIterations
print("Voting test data with ID3")
print(avgPerformance)
print(avgComparator)
#End Voting data


#Lenses Data!
lensesData = LensesData()
lensesData.loadData()
data = lensesData.rawData
target = lensesData.rawTarget

avgPerformance = 0
successfulIterations = 0
for i in range(0, 10):
    noError = True
    dtest, dtrain, ttest, ttrain = tts(data, target, train_size=.7, random_state=random.randint(100, 500))
    for item in dtrain:
        if len(item) != len(dtrain[0]):
            #print("The Heck???") tts seems to carry state from iteration to iteration
            noError = False
            break
    if noError == True:
        XPShell.m_data_test = dtest
        XPShell.m_data_train = dtrain
        XPShell.m_target_test = ttest
        XPShell.m_target_train = ttrain
        avgPerformance += XPShell.test()
        successfulIterations += 1

avgPerformance /= successfulIterations
print("Lenses test data with ID3")
print(avgPerformance)
#End Lenses data

#Car Data!
carData = CarData()
carData.loadData()
data = carData.rawData
target = carData.rawTarget

avgPerformance = 0
successfulIterations = 0
for i in range(0, 10):
    noError = True
    dtest, dtrain, ttest, ttrain = tts(data, target, train_size=.7, random_state=random.randint(100, 500))
    for item in dtrain:
        if len(item) != len(dtrain[0]):
            #print("The Heck???") tts seems to carry state from iteration to iteration
            noError = False
            break
    if noError == True:
        XPShell.m_data_test = dtest
        XPShell.m_data_train = dtrain
        XPShell.m_target_test = ttest
        XPShell.m_target_train = ttrain
        avgPerformance += XPShell.test()
        successfulIterations += 1

avgPerformance /= successfulIterations
print("Car test data with ID3")
print(avgPerformance)
#END CAR DATA
