import numpy as np
import xlrd
import random
def dataReader2(ncolsBegin, ncolsEnd, nrowsLength, stepNumber, nrowsBegin, setLabel, interval):
    data = xlrd.open_workbook('finaldata.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    useLabel = []
    while True:
        if nrowsBegin % interval < 7:
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
    dataLabel = ((data,) + (label,))
    return dataLabel
good = dataReader2(ncolsBegin=1, ncolsEnd=5, nrowsLength=100, stepNumber=1000, nrowsBegin=0, setLabel=0, interval=10)
a = good[0]
