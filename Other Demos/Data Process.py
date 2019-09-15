import numpy as np
import xlrd

data = xlrd.open_workbook('data.xlsx')
table = data.sheet_by_name('Sheet1')
data = []
for r in range(table.nrows):
    val = []
    for c in range(table.ncols):
        val.append(table.cell_value(r, c))
    data.append(tuple(val))
print(data)
#v00 = table.cell_value(0, 0)
#v01 = table.cell_value(0, 1)
#v02 = table.cell_value(0, 2)
#v03 = table.cell_value(0, 3)
#v10 = table.cell_value(1, 0)
#v11 = table.cell_value(1, 1)
#v12 = table.cell_value(1, 2)
#v13 = table.cell_value(1, 3)
#a = np.array([[v00, v01], [v10, v11]], dtype=float)
#b = np.array([[v02, v03], [v12, v13]], dtype=float)
#v = np.concatenate((a, b))



