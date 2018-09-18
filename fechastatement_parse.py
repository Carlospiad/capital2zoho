import xlrd
import csv
from datetime import datetime


book = xlrd.open_workbook("data/data.xlsx")
sh = book.sheet_by_index(0)

empty_cell= False

with xlrd.open_workbook("data/data.xlsx") as wb:
    with open('data/output.csv', 'w+') as csvout:
        cs= wb.sheet_by_index(0)
        num_cols= cs.ncols
        num_rows= cs.nrows
        writer = csv.writer(csvout, lineterminator='\n')
        writer.writerow(['Date', 'Payee','Concepto','Referencia', 'Outflow', 'Inflow']) # write new header
        for row_index in range(1, num_rows):

            writer.writerow((
                sh.cell_value(row_index, colx=0), #fecha
                '',
                sh.cell_value(row_index, colx=3),
                sh.cell_value(row_index, colx=1),
                "" if sh.cell_value(row_index, colx=7)=='-' else sh.cell_value(row_index, colx=7),
                "" if sh.cell_value(row_index, colx=8)=='-' else sh.cell_value(row_index, colx=8)
                ))


# with xlrd.open_workbook("data/data.xlsx") as wb:
#     with open('data/output.csv', 'w+') as csvout:
#         cs= wb.sheet_by_index(0)
#         num_cols= cs.ncols
#         num_rows= cs.nrows
#         writer = csv.writer(csvout, lineterminator='\n')
#         writer.writerow(['Date', 'Payee','Concepto','Referencia', 'Outflow', 'Inflow']) # write new header
#         for row_index in range(1, num_rows):
#
#             writer.writerow((
#                 sh.cell_value(row_index, colx=0), #fecha
#                 '',
#                 sh.cell_value(row_index, colx=3),
#                 sh.cell_value(row_index, colx=1),
#                 if sh.cell_value(row_index, colx=7)='-',
#                 sh.cell_value(row_index, colx=8)
#                 ))
