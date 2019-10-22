import xlrd
import numpy as np
data = xlrd.open_workbook('finaldata.xlsx')
table = data.sheet_by_name('Sheet1')
data = []
for c in range(100):
    val = []
    for r in range(1, 5):
        val.append(table.cell_value(c, r))
        data.append(tuple(val))
data = np.r_[data]
