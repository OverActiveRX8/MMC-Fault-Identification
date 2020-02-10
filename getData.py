import numpy as np
import xlrd


def dataReader(ncolsBegin, ncolsEnd, nrowsBegin, nrowsLength, stepNumber, setLabel):
    data = xlrd.open_workbook('igbt1break.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    useLabel = []
    newBegin = nrowsBegin
    while True:
        label = [setLabel]
        for c in range(nrowsBegin, nrowsBegin + nrowsLength):
            for r in range(ncolsBegin, ncolsEnd):
                val = [table.cell_value(c, r)]
                data.append(tuple(val))
        useLabel.append(tuple(label))
        nrowsBegin = nrowsBegin + 1
        if nrowsBegin == stepNumber:
            break
    data = np.reshape(np.r_[data], (stepNumber - newBegin, nrowsLength, ncolsEnd - ncolsBegin), order='C')
    useLabel = np.reshape(np.r_[useLabel], (stepNumber - newBegin, 1), order='C').astype(np.float64)
    return data, useLabel


def getData(locationx, locationy, stepNumber):
    data = xlrd.open_workbook('igbt1break.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    step = 0
    while True:
        for c in range(locationy, locationy + 200):
            for r in range(locationx, locationx + 6):
                val = [table.cell_value(c, r)]
                data.append(tuple(val))
        locationy += 1
        step += 1
        if step >= stepNumber:
            break
    data = np.reshape(np.r_[data], (step, 200, 6), order='C')
    return data  #


# 选个位置和组数，位置需从V1开始

def getLabel(setLabel, stepNumber):
    label = []
    useLabel = [setLabel]
    for labelNumber in range(0, stepNumber):
        label.append(tuple(useLabel))
    label = np.reshape(np.r_[label], (stepNumber, 1), order='C').astype(np.float64)
    return label


# 设置标签和组数

def normalization(x):
    _range = np.max(x) - np.min(x)
    return (x - np.min(x)) / _range


def trainData(igbt1ErrorTime, stepNumber):
    global trainError, trainGood
    if igbt1ErrorTime == 0.5:
        trainGood = getData(9, 5, stepNumber)
        trainError = getData(9, 5005, stepNumber)
        dataGroup = normalization(np.r_[trainGood, trainError]).reshape([2 * stepNumber, 200, 6])
        labelGroup = np.r_[getLabel(0, stepNumber), getLabel(1, stepNumber)]
        return dataGroup, labelGroup
    else:
        if 0.5 < igbt1ErrorTime <= 0.505:
            trainGood = getData(17, 5, stepNumber)
            trainError = getData(17, 5055, stepNumber)
            dataGroup = normalization(np.r_[trainGood, trainError]).reshape([2 * stepNumber, 200, 6])
            labelGroup = np.r_[getLabel(0, stepNumber), getLabel(1, stepNumber)]
            return dataGroup, labelGroup
        else:
            if 0.505 < igbt1ErrorTime <= 0.510:
                trainGood = getData(25, 5, stepNumber)
                trainError = getData(25, 5055, stepNumber)
                dataGroup = normalization(np.r_[trainGood, trainError]).reshape([2 * stepNumber, 200, 6])
                labelGroup = np.r_[getLabel(0, stepNumber), getLabel(1, stepNumber)]
                return dataGroup, labelGroup
            else:
                if 0.510 < igbt1ErrorTime <= 0.515:
                    trainGood = getData(33, 5, stepNumber)
                    trainError = getData(33, 5105, stepNumber)
                    dataGroup = normalization(np.r_[trainGood, trainError]).reshape([2 * stepNumber, 200, 6])
                    labelGroup = np.r_[getLabel(0, stepNumber), getLabel(1, stepNumber)]
                    return dataGroup, labelGroup
                else:
                    if 0.515 < igbt1ErrorTime <= 0.520:
                        trainGood = getData(41, 5, stepNumber)
                        trainError = getData(41, 5055, stepNumber)
                        dataGroup = normalization(np.r_[trainGood, trainError]).reshape([2 * stepNumber, 200, 6])
                        labelGroup = np.r_[getLabel(0, stepNumber), getLabel(1, stepNumber)]
                        return dataGroup, labelGroup
                    else:
                        print("please input another time")


# 设置故障时间，分别有从0.5s、0.505s、0.510s、0.515s、0.052开始的故障

u = trainData(0.505, 100)
