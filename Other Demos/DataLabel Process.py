import numpy as np
import xlrd
import pandas as pd

np.set_printoptions(suppress=True)


def dataReader2(ncolsBegin, ncolsEnd, nrowsLength, stepLength, stepNumber):
    data = xlrd.open_workbook('data.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    for r in range(ncolsBegin, ncolsEnd):
        i = 0
        while True:
            val = []
            for c in range(i, i + nrowsLength):
                val.append(table.cell_value(c, r))
            i = i + stepLength
            data.append(tuple(val))
            if i + nrowsLength == stepNumber:
                break
    dataNumpyType = np.r_[data]
    return dataNumpyType
names = locals()
for j in range(10):
    if j == 0:
        names['goodData' + str(j + 1) + 'A'] = dataReader2(ncolsBegin=j + 1, ncolsEnd=j + 2, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'B'] = dataReader2(ncolsBegin=j + 2, ncolsEnd=j + 3, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'C'] = dataReader2(ncolsBegin=j + 3, ncolsEnd=j + 4, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'D'] = dataReader2(ncolsBegin=j + 4, ncolsEnd=j + 5, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
    else:
        names['goodData' + str(j + 1) + 'A'] = dataReader2(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 7,
                                                           nrowsLength=100,stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'B'] = dataReader2(ncolsBegin=10 * (j - 1) + 7, ncolsEnd=10 * (j - 1) + 8,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'C'] = dataReader2(ncolsBegin=10 * (j - 1) + 8, ncolsEnd=10 * (j - 1) + 9,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        names['goodData' + str(j + 1) + 'D'] = dataReader2(ncolsBegin=10 * (j - 1) + 9, ncolsEnd=10 * (j - 1) + 10,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        #读取好数据，ABCD代表四个子模块的电压数据
names['errorData' + 'A' + str(1) + 'A'] = dataReader2(ncolsBegin=11, ncolsEnd=12, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'B'] = dataReader2(ncolsBegin=12, ncolsEnd=13, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'C'] = dataReader2(ncolsBegin=13, ncolsEnd=14, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'D'] = dataReader2(ncolsBegin=14, ncolsEnd=15, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(2) + 'A'] = dataReader2(ncolsBegin=21, ncolsEnd=22, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(2) + 'B'] = dataReader2(ncolsBegin=22, ncolsEnd=23, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(2) + 'C'] = dataReader2(ncolsBegin=23, ncolsEnd=24, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(2) + 'D'] = dataReader2(ncolsBegin=24, ncolsEnd=25, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'A'] = dataReader2(ncolsBegin=31, ncolsEnd=32, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'B'] = dataReader2(ncolsBegin=32, ncolsEnd=33, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'C'] = dataReader2(ncolsBegin=33, ncolsEnd=34, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'D'] = dataReader2(ncolsBegin=34, ncolsEnd=35, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(2) + 'A'] = dataReader2(ncolsBegin=41, ncolsEnd=42, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(2) + 'B'] = dataReader2(ncolsBegin=42, ncolsEnd=43, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(2) + 'C'] = dataReader2(ncolsBegin=43, ncolsEnd=44, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(2) + 'D'] = dataReader2(ncolsBegin=44, ncolsEnd=45, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'A'] = dataReader2(ncolsBegin=51, ncolsEnd=52, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'B'] = dataReader2(ncolsBegin=52, ncolsEnd=53, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'C'] = dataReader2(ncolsBegin=53, ncolsEnd=54, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'D'] = dataReader2(ncolsBegin=54, ncolsEnd=55, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(2) + 'A'] = dataReader2(ncolsBegin=61, ncolsEnd=62, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(2) + 'B'] = dataReader2(ncolsBegin=62, ncolsEnd=63, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(2) + 'C'] = dataReader2(ncolsBegin=63, ncolsEnd=64, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(2) + 'D'] = dataReader2(ncolsBegin=64, ncolsEnd=65, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'A'] = dataReader2(ncolsBegin=71, ncolsEnd=72, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'B'] = dataReader2(ncolsBegin=72, ncolsEnd=73, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'C'] = dataReader2(ncolsBegin=73, ncolsEnd=74, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'D'] = dataReader2(ncolsBegin=74, ncolsEnd=75, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(2) + 'A'] = dataReader2(ncolsBegin=81, ncolsEnd=82, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(2) + 'B'] = dataReader2(ncolsBegin=82, ncolsEnd=83, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(2) + 'C'] = dataReader2(ncolsBegin=83, ncolsEnd=84, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(2) + 'D'] = dataReader2(ncolsBegin=84, ncolsEnd=85, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
#读取坏数据，一共四个子模块，每个子模块两个ijbt分别故障
for n in range(10):
    names['dataGood' + str(n + 1) + 'A'] = pd.DataFrame(names['goodData' + str(n + 1) + 'A'])
    names['dataGood' + str(n + 1) + 'B'] = pd.DataFrame(names['goodData' + str(n + 1) + 'B'])
    names['dataGood' + str(n + 1) + 'C'] = pd.DataFrame(names['goodData' + str(n + 1) + 'C'])
    names['dataGood' + str(n + 1) + 'D'] = pd.DataFrame(names['goodData' + str(n + 1) + 'D'])
for q in range(1, 3):
    names['errorData' + 'A' + str(q) + 'A'] = pd.DataFrame(names['errorData' + 'A' + str(q) + 'A'])
    names['errorData' + 'A' + str(q) + 'B'] = pd.DataFrame(names['errorData' + 'A' + str(q) + 'B'])
    names['errorData' + 'A' + str(q) + 'C'] = pd.DataFrame(names['errorData' + 'A' + str(q) + 'C'])
    names['errorData' + 'A' + str(q) + 'D'] = pd.DataFrame(names['errorData' + 'A' + str(q) + 'D'])
    names['errorData' + 'B' + str(q) + 'A'] = pd.DataFrame(names['errorData' + 'B' + str(q) + 'A'])
    names['errorData' + 'B' + str(q) + 'B'] = pd.DataFrame(names['errorData' + 'B' + str(q) + 'B'])
    names['errorData' + 'B' + str(q) + 'C'] = pd.DataFrame(names['errorData' + 'B' + str(q) + 'C'])
    names['errorData' + 'B' + str(q) + 'D'] = pd.DataFrame(names['errorData' + 'B' + str(q) + 'D'])
    names['errorData' + 'C' + str(q) + 'A'] = pd.DataFrame(names['errorData' + 'C' + str(q) + 'A'])
    names['errorData' + 'C' + str(q) + 'B'] = pd.DataFrame(names['errorData' + 'C' + str(q) + 'B'])
    names['errorData' + 'C' + str(q) + 'C'] = pd.DataFrame(names['errorData' + 'C' + str(q) + 'C'])
    names['errorData' + 'C' + str(q) + 'D'] = pd.DataFrame(names['errorData' + 'C' + str(q) + 'D'])
    names['errorData' + 'D' + str(q) + 'A'] = pd.DataFrame(names['errorData' + 'D' + str(q) + 'A'])
    names['errorData' + 'D' + str(q) + 'B'] = pd.DataFrame(names['errorData' + 'D' + str(q) + 'B'])
    names['errorData' + 'D' + str(q) + 'C'] = pd.DataFrame(names['errorData' + 'D' + str(q) + 'C'])
    names['errorData' + 'D' + str(q) + 'D'] = pd.DataFrame(names['errorData' + 'D' + str(q) + 'D'])
#将好数据和坏数据转化成pandas索引表
print(dataGood7A)
for i in range(10):
    for x in range(1000):
        names['dataGood' + str(i + 1) + 'A'] = names['dataGood' + str(i + 1) + 'A'].rename(index={x: 1})
        names['dataGood' + str(i + 1) + 'B'] = names['dataGood' + str(i + 1) + 'B'].rename(index={x: 1})
        names['dataGood' + str(i + 1) + 'C'] = names['dataGood' + str(i + 1) + 'C'].rename(index={x: 1})
        names['dataGood' + str(i + 1) + 'D'] = names['dataGood' + str(i + 1) + 'D'].rename(index={x: 1})
        #打标签
    names['goodLabel' + str(i + 1) + 'A'] = np.array(names['dataGood' + str(i + 1) + 'A'].index)
    names['goodLabel' + str(i + 1) + 'B'] = np.array(names['dataGood' + str(i + 1) + 'B'].index)
    names['goodLabel' + str(i + 1) + 'C'] = np.array(names['dataGood' + str(i + 1) + 'C'].index)
    names['goodLabel' + str(i + 1) + 'D'] = np.array(names['dataGood' + str(i + 1) + 'D'].index)
    #将标签转换为矩阵格式
for q in range(1, 3):
    for x in range(1000):
        names['errorData' + 'A' + str(q) + 'A'] = names['errorData' + 'A' + str(q) + 'A'].rename(index={x: (q * 0.1 +
                                                                                                            0)})
        names['errorData' + 'A' + str(q) + 'B'] = names['errorData' + 'A' + str(q) + 'B'].rename(index={x: (q * 0.1 +
                                                                                                            0)})
        names['errorData' + 'A' + str(q) + 'C'] = names['errorData' + 'A' + str(q) + 'C'].rename(index={x: (q * 0.1 +
                                                                                                            0)})
        names['errorData' + 'A' + str(q) + 'D'] = names['errorData' + 'A' + str(q) + 'D'].rename(index={x: (q * 0.1 +
                                                                                                            0)})
        names['errorData' + 'B' + str(q) + 'A'] = names['errorData' + 'B' + str(q) + 'A'].rename(index={x: (q * 0.1 +
                                                                                                            0.2)})
        names['errorData' + 'B' + str(q) + 'B'] = names['errorData' + 'B' + str(q) + 'B'].rename(index={x: (q * 0.1 +
                                                                                                            0.2)})
        names['errorData' + 'B' + str(q) + 'C'] = names['errorData' + 'B' + str(q) + 'C'].rename(index={x: (q * 0.1 +
                                                                                                            0.2)})
        names['errorData' + 'B' + str(q) + 'D'] = names['errorData' + 'B' + str(q) + 'D'].rename(index={x: (q * 0.1 +
                                                                                                            0.2)})
        names['errorData' + 'C' + str(q) + 'A'] = names['errorData' + 'C' + str(q) + 'A'].rename(index={x: (q * 0.1 +
                                                                                                            0.4)})
        names['errorData' + 'C' + str(q) + 'B'] = names['errorData' + 'C' + str(q) + 'B'].rename(index={x: (q * 0.1 +
                                                                                                            0.4)})
        names['errorData' + 'C' + str(q) + 'C'] = names['errorData' + 'C' + str(q) + 'C'].rename(index={x: (q * 0.1 +
                                                                                                            0.4)})
        names['errorData' + 'C' + str(q) + 'D'] = names['errorData' + 'C' + str(q) + 'D'].rename(index={x: (q * 0.1 +
                                                                                                            0.4)})
        names['errorData' + 'D' + str(q) + 'A'] = names['errorData' + 'D' + str(q) + 'A'].rename(index={x: (q * 0.1 +
                                                                                                            0.6)})
        names['errorData' + 'D' + str(q) + 'B'] = names['errorData' + 'D' + str(q) + 'B'].rename(index={x: (q * 0.1 +
                                                                                                            0.6)})
        names['errorData' + 'D' + str(q) + 'C'] = names['errorData' + 'D' + str(q) + 'C'].rename(index={x: (q * 0.1 +
                                                                                                            0.6)})
        names['errorData' + 'D' + str(q) + 'D'] = names['errorData' + 'D' + str(q) + 'D'].rename(index={x: (q * 0.1 +
                                                                                                            0.6)})
    names['errorLabel' + 'A' + str(q) + 'A'] = np.array(names['errorData' + 'A' + str(q) + 'A'].index)
    names['errorLabel' + 'A' + str(q) + 'B'] = np.array(names['errorData' + 'A' + str(q) + 'B'].index)
    names['errorLabel' + 'A' + str(q) + 'C'] = np.array(names['errorData' + 'A' + str(q) + 'C'].index)
    names['errorLabel' + 'A' + str(q) + 'D'] = np.array(names['errorData' + 'A' + str(q) + 'D'].index)
    names['errorLabel' + 'B' + str(q) + 'A'] = np.array(names['errorData' + 'B' + str(q) + 'A'].index)
    names['errorLabel' + 'B' + str(q) + 'B'] = np.array(names['errorData' + 'B' + str(q) + 'B'].index)
    names['errorLabel' + 'B' + str(q) + 'C'] = np.array(names['errorData' + 'B' + str(q) + 'C'].index)
    names['errorLabel' + 'B' + str(q) + 'D'] = np.array(names['errorData' + 'B' + str(q) + 'D'].index)
    names['errorLabel' + 'C' + str(q) + 'A'] = np.array(names['errorData' + 'C' + str(q) + 'A'].index)
    names['errorLabel' + 'C' + str(q) + 'B'] = np.array(names['errorData' + 'C' + str(q) + 'B'].index)
    names['errorLabel' + 'C' + str(q) + 'C'] = np.array(names['errorData' + 'C' + str(q) + 'C'].index)
    names['errorLabel' + 'C' + str(q) + 'D'] = np.array(names['errorData' + 'C' + str(q) + 'D'].index)
    names['errorLabel' + 'D' + str(q) + 'A'] = np.array(names['errorData' + 'D' + str(q) + 'A'].index)
    names['errorLabel' + 'D' + str(q) + 'B'] = np.array(names['errorData' + 'D' + str(q) + 'B'].index)
    names['errorLabel' + 'D' + str(q) + 'C'] = np.array(names['errorData' + 'D' + str(q) + 'C'].index)
    names['errorLabel' + 'D' + str(q) + 'D'] = np.array(names['errorData' + 'D' + str(q) + 'D'].index)

print(errorDataA1A)
print(errorLabelA1A)

