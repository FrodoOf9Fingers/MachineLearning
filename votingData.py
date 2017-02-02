from usefulFunctions import loadCSV

class VotingData:
    rawData = []
    rawTarget = []
    rawCSV = []

    def loadData(self):
        self.rawCSV = loadCSV("voting.csv")
        for item in self.rawCSV:
            self.rawData.append(item[:-1])
            self.rawTarget.append(item[-1])
        return