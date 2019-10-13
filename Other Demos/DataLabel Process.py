import names as names
import numpy as np
import xlrd

np.set_printoptions(suppress=True)


def dataReader2(ncolsBegin, ncolsEnd, nrowsLength, stepLength, stepNumber):
    data = xlrd.open_workbook('finaldata.xlsx')
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
        names['goodData' + str(j) + 'A'] = dataReader2(ncolsBegin=j + 1, ncolsEnd=j + 2, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'B'] = dataReader2(ncolsBegin=j + 2, ncolsEnd=j + 3, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'C'] = dataReader2(ncolsBegin=j + 3, ncolsEnd=j + 4, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'D'] = dataReader2(ncolsBegin=j + 4, ncolsEnd=j + 5, nrowsLength=100,
                                                           stepLength=1, stepNumber=1000)
    else:
        names['goodData' + str(j) + 'A'] = dataReader2(ncolsBegin=10 * (j - 1) + 6, ncolsEnd=10 * (j - 1) + 7,
                                                           nrowsLength=100,stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'B'] = dataReader2(ncolsBegin=10 * (j - 1) + 7, ncolsEnd=10 * (j - 1) + 8,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'C'] = dataReader2(ncolsBegin=10 * (j - 1) + 8, ncolsEnd=10 * (j - 1) + 9,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        names['goodData' + str(j) + 'D'] = dataReader2(ncolsBegin=10 * (j - 1) + 9, ncolsEnd=10 * (j - 1) + 10,
                                                           nrowsLength=100, stepLength=1, stepNumber=1000)
        #读取好数据，ABCD代表四个子模块的电压数据
names['errorData' + 'A' + str(0) + 'A'] = dataReader2(ncolsBegin=11, ncolsEnd=12, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(0) + 'B'] = dataReader2(ncolsBegin=12, ncolsEnd=13, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(0) + 'C'] = dataReader2(ncolsBegin=13, ncolsEnd=14, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(0) + 'D'] = dataReader2(ncolsBegin=14, ncolsEnd=15, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'A'] = dataReader2(ncolsBegin=21, ncolsEnd=22, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'B'] = dataReader2(ncolsBegin=22, ncolsEnd=23, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'C'] = dataReader2(ncolsBegin=23, ncolsEnd=24, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'A' + str(1) + 'D'] = dataReader2(ncolsBegin=24, ncolsEnd=25, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(0) + 'A'] = dataReader2(ncolsBegin=31, ncolsEnd=32, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(0) + 'B'] = dataReader2(ncolsBegin=32, ncolsEnd=33, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(0) + 'C'] = dataReader2(ncolsBegin=33, ncolsEnd=34, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(0) + 'D'] = dataReader2(ncolsBegin=34, ncolsEnd=35, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'A'] = dataReader2(ncolsBegin=41, ncolsEnd=42, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'B'] = dataReader2(ncolsBegin=42, ncolsEnd=43, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'C'] = dataReader2(ncolsBegin=43, ncolsEnd=44, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'B' + str(1) + 'D'] = dataReader2(ncolsBegin=44, ncolsEnd=45, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(0) + 'A'] = dataReader2(ncolsBegin=51, ncolsEnd=52, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(0) + 'B'] = dataReader2(ncolsBegin=52, ncolsEnd=53, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(0) + 'C'] = dataReader2(ncolsBegin=53, ncolsEnd=54, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(0) + 'D'] = dataReader2(ncolsBegin=54, ncolsEnd=55, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'A'] = dataReader2(ncolsBegin=61, ncolsEnd=62, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'B'] = dataReader2(ncolsBegin=62, ncolsEnd=63, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'C'] = dataReader2(ncolsBegin=63, ncolsEnd=64, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'C' + str(1) + 'D'] = dataReader2(ncolsBegin=64, ncolsEnd=65, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(0) + 'A'] = dataReader2(ncolsBegin=71, ncolsEnd=72, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(0) + 'B'] = dataReader2(ncolsBegin=72, ncolsEnd=73, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(0) + 'C'] = dataReader2(ncolsBegin=73, ncolsEnd=74, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(0) + 'D'] = dataReader2(ncolsBegin=74, ncolsEnd=75, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'A'] = dataReader2(ncolsBegin=81, ncolsEnd=82, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'B'] = dataReader2(ncolsBegin=82, ncolsEnd=83, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'C'] = dataReader2(ncolsBegin=83, ncolsEnd=84, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
names['errorData' + 'D' + str(1) + 'D'] = dataReader2(ncolsBegin=84, ncolsEnd=85, nrowsLength=100, stepLength=1,
                                                      stepNumber=1000)
#读取坏数据，一共四个子模块，每个子模块两个ijbt分别故障
for x in range(10):
    names['good' + str(x) + 'A'] = ()
    names['good' + str(x) + 'B'] = ()
    names['good' + str(x) + 'C'] = ()
    names['good' + str(x) + 'D'] = ()
    for n in range(900):
        names['good' + str(x) + 'A'] = names['good' + str(x) + 'A'] + ((names['goodData' + str(x) + 'A'][n],) +
                                                                       (np.array([0]),),)
        names['good' + str(x) + 'B'] = names['good' + str(x) + 'B'] + ((names['goodData' + str(x) + 'B'][n],) +
                                                                       (np.array([0]),),)
        names['good' + str(x) + 'C'] = names['good' + str(x) + 'C'] + ((names['goodData' + str(x) + 'C'][n],) +
                                                                       (np.array([0]),),)
        names['good' + str(x) + 'D'] = names['good' + str(x) + 'D'] + ((names['goodData' + str(x) + 'D'][n],) +
                                                                       (np.array([0]),),)
for x in range(2):
    names['error' + 'A' + str(x) + 'A'] = ()
    names['error' + 'A' + str(x) + 'B'] = ()
    names['error' + 'A' + str(x) + 'C'] = ()
    names['error' + 'A' + str(x) + 'D'] = ()
    for n in range(900):
        names['error' + 'A' + str(x) + 'A'] = names['error' + 'A' + str(x) + 'A'] + (
            (names['errorData' + 'A' + str(x) + 'A'],) + (np.array([1]),),)
        names['error' + 'A' + str(x) + 'B'] = names['error' + 'A' + str(x) + 'B'] + (
            (names['errorData' + 'A' + str(x) + 'B'],) + (np.array([1]),),)
        names['error' + 'A' + str(x) + 'C'] = names['error' + 'A' + str(x) + 'C'] + (
            (names['errorData' + 'A' + str(x) + 'C'],) + (np.array([1]),),)
        names['error' + 'A' + str(x) + 'D'] = names['error' + 'A' + str(x) + 'D'] + (
            (names['errorData' + 'A' + str(x) + 'D'],) + (np.array([1]),),)
for x in range(2):
    names['error' + 'B' + str(x) + 'A'] = ()
    names['error' + 'B' + str(x) + 'B'] = ()
    names['error' + 'B' + str(x) + 'C'] = ()
    names['error' + 'B' + str(x) + 'D'] = ()
    for n in range(900):
        names['error' + 'B' + str(x) + 'A'] = names['error' + 'B' + str(x) + 'A'] + (
            (names['errorData' + 'B' + str(x) + 'A'],) + (np.array([1]),),)
        names['error' + 'B' + str(x) + 'B'] = names['error' + 'B' + str(x) + 'B'] + (
            (names['errorData' + 'B' + str(x) + 'B'],) + (np.array([1]),),)
        names['error' + 'B' + str(x) + 'C'] = names['error' + 'B' + str(x) + 'C'] + (
            (names['errorData' + 'B' + str(x) + 'C'],) + (np.array([1]),),)
        names['error' + 'B' + str(x) + 'D'] = names['error' + 'B' + str(x) + 'D'] + (
            (names['errorData' + 'B' + str(x) + 'D'],) + (np.array([1]),),)

for x in range(2):
    names['error' + 'C' + str(x) + 'A'] = ()
    names['error' + 'C' + str(x) + 'B'] = ()
    names['error' + 'C' + str(x) + 'C'] = ()
    names['error' + 'C' + str(x) + 'D'] = ()
    for n in range(900):
        names['error' + 'C' + str(x) + 'A'] = names['error' + 'C' + str(x) + 'A'] + (
            (names['errorData' + 'C' + str(x) + 'A'],) + (np.array([1]),),)
        names['error' + 'C' + str(x) + 'B'] = names['error' + 'C' + str(x) + 'B'] + (
            (names['errorData' + 'C' + str(x) + 'B'],) + (np.array([1]),),)
        names['error' + 'C' + str(x) + 'C'] = names['error' + 'C' + str(x) + 'C'] + (
            (names['errorData' + 'C' + str(x) + 'C'],) + (np.array([1]),),)
        names['error' + 'C' + str(x) + 'D'] = names['error' + 'C' + str(x) + 'D'] + (
            (names['errorData' + 'C' + str(x) + 'D'],) + (np.array([1]),),)

for x in range(2):
    names['error' + 'D' + str(x) + 'A'] = ()
    names['error' + 'D' + str(x) + 'B'] = ()
    names['error' + 'D' + str(x) + 'C'] = ()
    names['error' + 'D' + str(x) + 'D'] = ()
    for n in range(900):
        names['error' + 'D' + str(x) + 'A'] = names['error' + 'D' + str(x) + 'A'] + (
            (names['errorData' + 'D' + str(x) + 'A'],) + (np.array([1]),),)
        names['error' + 'D' + str(x) + 'B'] = names['error' + 'D' + str(x) + 'B'] + (
            (names['errorData' + 'D' + str(x) + 'B'],) + (np.array([1]),),)
        names['error' + 'D' + str(x) + 'C'] = names['error' + 'D' + str(x) + 'C'] + (
            (names['errorData' + 'D' + str(x) + 'C'],) + (np.array([1]),),)
        names['error' + 'D' + str(x) + 'D'] = names['error' + 'D' + str(x) + 'D'] + (
            (names['errorData' + 'D' + str(x) + 'D'],) + (np.array([1]),),)
print(errorA1A)
print(errorB0C)
print(good3A)