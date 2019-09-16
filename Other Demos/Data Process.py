import numpy as np
import xlrd

def dataReader2(ncolsLenght):
    data = xlrd.open_workbook('data.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    for r in range(table.nrows):
        val = []
        for c in range(ncolsLenght):
            val.append(table.cell_value(r, c))
        data.append(tuple(val))
    dataNumpyType = np.r_[data]
    print(dataNumpyType)
    return
dataReader2(ncolsLenght=5)
