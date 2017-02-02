from math import log2

class dTreeNode:

    branches = {}
    split_col = -1
    target = ''
    default = ''

    def __init__(self):
        self.branches = {}
        self.split_col = -1
        self.target = ''

    def spawn(self, data):
        #For Base Case testing
        #Key = target, Value = occurrences
        dict = {}
        for i in range(0, len(data)):
            if not(data[i][len(data[0]) -1] in dict):
                dict[data[i][len(data[0]) -1]] = 0
            dict[data[i][len(data[0]) -1]] += 1

        #Base Case: only target column remains
        if (len(data[0]) == 1):
            self.target = max(dict, key=dict.get)
            return

        # Base Case: entropy = 0
        if (len(dict) <= 1):
            self.target = list(dict.keys())[0]
            return

        #Set Default
        self.default = max(dict, key=dict.get)

        self.split_col = self.find_best_attribute(data)

        #Key = columnValueType, Value = rows
        dataForBranches = {}
        for i in range(0, len(data)):
            if not(data[i][self.split_col] in dataForBranches):  # If the attribute has this value
                dataForBranches[data[i][self.split_col]] = []
            dataForBranches[data[i][self.split_col]].append(data[i])

        pairList = list(dataForBranches.items())
        for item in pairList:
            branch = dTreeNode()
            self.branches[item[0]] = branch
            branch.spawn(self.remove_col(item[1], self.split_col))

    def remove_col(self, data, col):
        newData = []
        for i in range(0, len(data)):
            newData.append([])
            for j in range(0, len(data[0])):
                if j == col:
                    continue
                newData[i].append(data[i][j])
        return newData

    def find_best_attribute(self, data):
        attributes = []
        attribute = 0
        for col in range(0, len(data[0]) - 1):
            attributes.append(self.solve_attribute(data, col))
        attribute = sorted(attributes, key=lambda x: x[1])[0] #Python automatically use min between the first elements of the lists
        return attribute[0]

    def solve_attribute(self, data, col):
        #Key = columnValueType, Value = Dictionary (Key = targetValue, Value = occurrences
        dict = {}
        for i in range(0, len(data)):
            if data[i][col] in dict:  #If the attribute has this value
                if data[i][len(data[i]) - 1] in dict[data[i][col]]: #If the value of this attribute has this target
                    dict[data[i][col]][data[i][len(data[i]) - 1]] += 1
                else:
                    dict[data[i][col]][data[i][len(data[i]) - 1]] = 1
            else:
                dict[data[i][col]] = {}
                dict[data[i][col]][data[i][len(data[i]) - 1]] = 1
        return (col, self.calc_attribute_entropy(dict))

    def calc_attribute_entropy(self, dict):
        #Count rows in attributes
        pairList = list(dict.items())
        numItems = 0
        for i in range(0, len(pairList)):
            numItems += self.count_items(pairList[i])
        #Calc entropy of each attribute, weight it according to number of items, and add to retval
        retval = 0
        for i in range(0, len(pairList)):
            retval += self.calc_entropy(pairList[i]) * self.count_items(pairList[i]) / numItems
        return retval

    def count_items(self, dictTuple):
        pairList = list(dictTuple[1].items())
        retval = 0
        for i in range(0, len(pairList)):
            retval += pairList[i][1]
        return retval

    def find(self, row):
        if self.target != '':
            return self.target
        else:
            childRow = list(row)
            del childRow[self.split_col]
            if row[self.split_col] in self.branches:
                return self.branches[row[self.split_col]].find(childRow)
            else:
                return self.default

    def calc_entropy(self, dictTuple):
        pairList = list(dictTuple[1].items())
        entropy = 0
        totalItems = 0;
        for item in pairList:
            totalItems += item[1]
        for i in range(0, len(pairList)):
            entropy += -1 * (pairList[i][1] / totalItems) * log2(pairList[i][1] / totalItems)
        return entropy

    def string_rep(self, header, depth):
        if self.target == '':
            childList = list(header)
            childList.remove(childList[self.split_col])
            representation = "Branch:" + header[self.split_col] + "\n"
            for item in self.branches.items():
                representation += ('  ' * (depth + 1)) + str(item[0]) + '\n' + ('  ' * (depth + 1)) + item[1].string_rep(childList, depth + 1)
        else:
            representation = ": " + self.target + "\n"
        return representation

class iD3Classifier:
    dTree = dTreeNode()

    def train(self, train_data, train_target):
        #refresh dTree
        self.dTree = dTreeNode()

        #attach target to data
        data = list(train_data)
        for i in range(0, len(data)):
            data[i].append(train_target[i])

        #Spawn the tree!
        self.dTree.spawn(data)
        return

    def predict(self, test_item):
        return self.dTree.find(test_item)

    def printTree(self, header):
        print(self.dTree.string_rep(header, 0))
        return