from usefulFunctions import loadCSV

class LensesData:
    rawData = []
    rawTarget = []
    rawCSV = []

    def loadData(self):
        self.rawCSV = loadCSV("lenses.csv")
        for item in self.rawCSV:
            self.rawData.append(item[:-1])
            self.rawTarget.append(item[-1])
        return