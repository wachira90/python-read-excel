#!python
import xlrd
import os
import sys

loc = ('file1.xlsx')

wb = xlrd.open_workbook(loc)
# wb = xlrd.open_workbook("file1.xlsx")
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

for c in range(sheet.ncols):
    for r in range(sheet.nrows):
        if (sheet.ncols == "2"):
            print(sheet.cell_value(r, c), end='')
        else:
            print(sheet.cell_value(r, c), end='|')

# print("=> ", sheet.ncols)
