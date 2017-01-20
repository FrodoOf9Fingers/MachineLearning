class kNNClassifier:
    m_data = []
    m_target = []
    k = 0

    def train(self, train_data, train_target):
        self.m_data = train_data
        self.m_target = train_target
        return

    def predict(self, test_item):
        distances = [[[] for i in range(2)] for i in range(len(self.m_data))]
        for i in range(0, len(self.m_data)):
            distances[i][0] = self.calc_distance(self.m_data[i], test_item)
            distances[i][1] = self.m_target[i]
        distances.sort(key=lambda x: x[0]) #sort by the first index (distance)
        del distances[self.k] #delete all but the first k instances
        return self.find_most_common(distances)

    def calc_distance(self, v1, v2):
        distance = 0
        for i in range(0, len(v1)):
            distance += (v1[i] - v2[i])**2
        return distance

    def find_most_common(self, some2DList):
        someList = []
        for i in range(0, self.k):
            someList.append(some2DList[1])
        return max(someList, key=someList.count)[1]