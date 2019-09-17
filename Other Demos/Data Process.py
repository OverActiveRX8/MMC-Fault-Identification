import numpy as np
import xlrd

def dataReader2(nrowsLength, stepLength, stepNumber):
    data = xlrd.open_workbook('data.xlsx')
    table = data.sheet_by_name('Sheet1')
    data = []
    for r in range(table.ncols):
        i = 0
        while True:
            val = []
            for c in range(i, i + nrowsLength):
                val.append(table.cell_value(c, r))
            i = i + stepLength
            data.append(tuple(val))
            if i == stepNumber:
                break
    dataNumpyType = np.r_[data]
    print(dataNumpyType)
    return
dataReader2(nrowsLength=100, stepLength=1, stepNumber=100)
#data = xlrd.open_workbook('np.xls')
#table = data.sheet_by_name('Sheet1')
#data = []
#for r in range(table.ncols):
 #   i = 0
  #  while True:
   #     val = []
    #    for c in range(i, i + 3):
     #       val.append(table.cell_value(c, r))
      #  i = i + 1
       # data.append(tuple(val))
        #if i == 3:
         #   break
#dataNumpyType = np.r_[data]
#print(dataNumpyType)