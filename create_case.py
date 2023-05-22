#create training case in test_case.xlsx
#initialize excel object

import openpyxl
import random

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet['A1'] = 'x1'
worksheet['B1'] = 'x2'
worksheet['C1'] = 'x3'
worksheet['D1'] = 'y'

for i in range(1000):
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    worksheet['A'+str(i+2)] = a
    worksheet['B'+str(i+2)] = b
    worksheet['C'+str(i+2)] = c
    worksheet['D'+str(i+2)] = a+2*b+3*c

workbook.save('test_case.xlsx')