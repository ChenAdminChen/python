import xlrd
import xlutils
import xlwt
from xlwt import *
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time

#wbk = xlwt.Workbook()
#sheet2 =  wbk.add_sheet('sheet 2', cell_overwrite_ok=True)

#for r in range(0,10):  #row
    #for c in range(0, 10): #col

        #sheet2.write(r,c,'some text'+str(r))

#wbk.save(r'E:\test.xlsx')
data = [{'user_id':11,'subject_name':'f1','grade':99},{'user_id':12,'subject_name':'f2','grade':97},{'user_id':13,'subject_name':'f3','grade':59}]

path=r'E:\file.xlsx'

rb = open_workbook(path)
rs = rb.sheet_by_index(0)   #通过sheet_by_index()获取的sheet:通过索引得到第一张表单，也可以通过名

colnames = rs.row_values(0)

# 字：rs = rb.sheet_by_name(u'Sheet1')
wb=copy(rb)
ws=wb.get_sheet(0)        #通过get_sheet()获取的sheet,此时有write()方法

ncols=rs.ncols
nrows = rs.nrows

ws.write(0,0,'方法')
for r in range(2,nrows):  #row
    if r % 2 == 0:
        ws.write(r,0,'成')
    else:
        ws.write(r, 0, '不')

wb.save(r'E:\report1.xls')

