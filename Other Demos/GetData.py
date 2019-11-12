
import numpy as np
import xlrd

def dataReader(ncolsBegin, ncolsEnd, nrowsLength, stepNumber, nrowsBegin, setLabel, interval):
    data = xlrd.open_workbook('finaldata.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    useLabel = []
    while True:
        if nrowsBegin % interval > 5:
            label = [setLabel]
            for c in range(nrowsBegin, nrowsBegin + nrowsLength):
                for r in range(ncolsBegin, ncolsEnd):
                    val = []
                    val.append(table.cell_value(c, r))
                    data.append(tuple(val))
            useLabel.append(tuple(label))
        else:
            label = [abs(setLabel - 1)]
            for c in range(nrowsBegin, nrowsBegin + nrowsLength):
                for r in range(ncolsBegin + 5, ncolsEnd + 5):
                    val = []
                    val.append(table.cell_value(c, r))
                    data.append(tuple(val))
            useLabel.append(tuple(label))
        nrowsBegin = nrowsBegin + 1
        if nrowsBegin == stepNumber:
            break
    labelNumpyYype = np.r_[useLabel]
    dataNumpyType = np.r_[data]
    data = np.reshape(dataNumpyType, (stepNumber, nrowsLength, ncolsEnd - ncolsBegin), order='C')
    useLabel = np.reshape(labelNumpyYype, (stepNumber, 1), order='C')
    useLabel = useLabel.astype(np.float64)
    dataLabel = ((data,) + (useLabel,))
    return dataLabel


def dataReader2(ncolsBegin, ncolsEnd, nrowsLength, stepNumber, nrowsBegin, setLabel, interval):
    data = xlrd.open_workbook('finaldata.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    useLabel = []
    while True:
        if nrowsBegin % interval < 5:
            label = [0]
            for c in range(nrowsBegin, nrowsBegin + nrowsLength):
                for r in range(ncolsBegin, ncolsEnd):
                    val = []
                    val.append(table.cell_value(c, r))
                    data.append(tuple(val))
            useLabel.append(tuple(label))
        else:
            label = [setLabel]
            for c in range(nrowsBegin, nrowsBegin + nrowsLength):
                for r in range(ncolsBegin + 5, ncolsEnd + 5):
                    val = []
                    val.append(table.cell_value(c, r))
                    data.append(tuple(val))
            useLabel.append(tuple(label))
        nrowsBegin = nrowsBegin + 1
        if nrowsBegin == stepNumber:
            break
    labelNumpyYype = np.r_[useLabel]
    dataNumpyType = np.r_[data]
    data = np.reshape(dataNumpyType, (stepNumber, nrowsLength, ncolsEnd - ncolsBegin), order='C')
    useLabel = np.reshape(labelNumpyYype, (stepNumber, 1), order='C')
    useLabel = useLabel.astype(np.int8)
    dataLabel = ((data,) + (useLabel,))
    return dataLabel
names = locals()
for j in range(1, 9):
    names['trainData' + str(j)] = dataReader2(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 10,
                                              nrowsLength=100, stepNumber=1000, nrowsBegin=0, setLabel=j, interval=10)
    names['testData' + str(j)] = dataReader(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 10,
                                            nrowsLength=100, stepNumber=1000, nrowsBegin=0, setLabel=j, interval=10)

for i in range(1, 9):
    if i == 1:
        trainD = names['trainData' + str(i)][0]
        trainL = names['trainData' + str(i)][1]
        testD = names['testData' + str(i)][0]
        testL = names['testData' + str(i)][1]
    else:
        trainD = np.r_[trainD, names['trainData' + str(i)][0]]
        trainL = np.r_[trainL, names['trainData' + str(i)][1]]
        testD = np.r_[testD, names['testData' + str(i)][0]]
        testL = np.r_[testL, names['testData' + str(i)][1]]
def trainData():
    trainData = (trainD, trainL)
    return trainData
def testData():
    testData = (testD, testL)
    return testData
tr = trainData()
ts = testData()
