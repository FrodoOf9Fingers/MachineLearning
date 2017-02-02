class ExperimentShell:
    m_classifier = 0
    m_comparator = 0
    m_debug = 0

    m_data_train = []
    m_data_test = []
    m_target_train = []
    m_target_test = []
    def setClassifier(self, classifier):
        self.m_classifier = classifier

    def test(self):
        self.m_classifier.train(self.m_data_train, self.m_target_train)
        numRight = 0
        for i in range(0, len(self.m_data_test)):
            if self.m_classifier.predict(self.m_data_test[i]) == self.m_target_test[i]:
                numRight += 1
            if self.m_debug == 1:
                print(self.m_classifier.predict(self.m_data_test[i]))
        return numRight / len(self.m_data_test)

    def testComparator (self):
        self.m_comparator.fit(self.m_data_train, self.m_target_train)
        numRight = 0
        for i in range(0, len(self.m_data_test)):
            if self.m_comparator.predict(self.m_data_test[i]) == self.m_target_test[i]:
                numRight += 1
            if self.m_debug == 1:
                print(self.m_comparator.predict(self.m_data_test[i]))
        return numRight / len(self.m_data_test)