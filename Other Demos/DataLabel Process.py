import names as names
import numpy as np
import xlrd
import pandas as pd

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
names = locals()
for j in range(1, 9):
    names['trainData' + str(j)] = dataReader2(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 10,
                                              nrowsLength=100, stepNumber=1000, nrowsBegin=0, setLabel=0, interval=10)
    names['testData' + str(j)] = dataReader(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 10,
                                            nrowsLength=100, stepNumber=1000, nrowsBegin=0, setLabel=0, interval=10)
        #读取好数据，ABCD代表四个子模块的电压数据
#读取坏数据，一共四个子模块，每个子模块两个ijbt分别故障

