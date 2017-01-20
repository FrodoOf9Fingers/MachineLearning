from sklearn import datasets
from experimentShell import ExperimentShell
from HardCodedClassifier import hardCodedClassifer
import random
from sklearn.cross_validation import train_test_split as tts


iris = datasets.load_iris()
classifier = hardCodedClassifer()
XPShell = ExperimentShell()
XPShell.setClassifier(classifier)

XPShell.m_data_test, \
XPShell.m_data_train, \
XPShell.m_target_test, \
XPShell.m_target_train = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(100, 500))

print(XPShell.test(iris))