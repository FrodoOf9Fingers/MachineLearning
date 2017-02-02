from carData import CarData
from ID3Classifier import iD3Classifier

rawData = CarData()
rawData.loadData()
data = rawData.rawData
target = rawData.rawTarget

#classifier = iD3Classifier()
#classifier.train(data, target)
#classifier.printTree(['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6'])

a = [1, 2, 3, 4]
b = list(a)
b.append(5)


#dict = {'awesome' : 50}
#print('awesome' in dict)
