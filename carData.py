from usefulFunctions import loadCSV

class CarData:
    rawData = []
    rawTarget = []
    rawCSV = []

    def loadData(self):
        self.rawCSV = loadCSV("cars.csv")
        for item in self.rawCSV:
            self.rawData.append(item[:-1])
            self.rawTarget.append(item[-1])
        return

    def lowHighConvert(self, x):
        return {
            'low': 1,
            'med': 2,
            'high': 3,
            'vhigh': 4,
        }.get(x, 0)  # default to 0

    def carsC2(self, x):
        return {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5more': 5
        }.get(x, 0)  # default to 0

    def carsC3(self, x):
        return {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            'more': 5
        }.get(x, 0)  # default to 0

    def carsC4(self, x):
        return {
            'big': 3,
            'med': 2,
            'small': 1,
        }.get(x, 0)  # default to 0

    def carsTarget(self, x):
        return {
            'unacc': 1,
            'acc': 2,
            'good': 3,
            'vgood': 4
        }.get(x, 0)  # default to 0

    def denormCarData(self):
        data = [[0 for y in range(0, len(self.rawCSV[0]))] for x in range(0, len(self.rawCSV))]
        target = [0 for x in range(0, len(self.rawCSV))]
        for i in range(0, len(self.rawCSV)):
            data[i][0] = self.lowHighConvert(self.rawCSV[i][0])
            data[i][1] = self.lowHighConvert(self.rawCSV[i][1])
            data[i][2] = self.carsC2(self.rawCSV[i][2])
            data[i][3] = self.carsC3(self.rawCSV[i][3])
            data[i][4] = self.carsC4(self.rawCSV[i][4])
            data[i][5] = self.lowHighConvert(self.rawCSV[i][5])
            target[i] = self.carsTarget(self.rawCSV[i][6])
        return data, target
