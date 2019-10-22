import numpy as np
names = locals()
for i in range(3):
    names['gg' + str(i)] = np.array([[i, i + 1, i + 2], [i + 1, i + 2, i + 3]])
print(gg1)
print(gg1[1])
tuples = ()
for j in range(2):
    tuples = tuples + (((gg0[j],) + (gg1[j],)),)
print(tuples)
a = np.array([1, 2, 3])
print(a)
tuples2 = ((tuples) + (np.array([0.0]),))
print(tuples2)
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
names['goodData' + str(j) + 'B'] = dataReader2(ncolsBegin=j + 2, ncolsEnd=j + 3, nrowsLength=100,
                                               stepLength=1, stepNumber=1000)
names['goodData' + str(j) + 'C'] = dataReader2(ncolsBegin=j + 3, ncolsEnd=j + 4, nrowsLength=100,
                                               stepLength=1, stepNumber=1000)
names['goodData' + str(j) + 'D'] = dataReader2(ncolsBegin=j + 4, ncolsEnd=j + 5, nrowsLength=100,
                                               stepLength=1, stepNumber=1000)
for i in range(1000):
    if i == 0:
        good = dataReader2(ncolsBegin=1, ncolsEnd=5, nrowsLength=100, nrowBegin=i)
        data1 = good
    else:
        good = dataReader2(ncolsBegin=1, ncolsEnd=5, nrowsLength=100, nrowBegin=i)
        data1 = np.vstack([data1, good])
print(data1)
def dataReader2(ncolsBegin, ncolsEnd, nrowsLength, nrowBegin):
    data = xlrd.open_workbook('finaldata.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    for r in range(ncolsBegin, ncolsEnd):
        val = []
        for c in range(nrowBegin, nrowBegin + nrowsLength):
            val.append(table.cell_value(c, r))
        data.append(tuple(val))
    dataNumpyType = np.r_[data].T
    return dataNumpyType