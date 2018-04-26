# -*- coding: utf-8 -*-
import  xdrlib ,sys
import xlrd
def open_excel1(file= r'E:\file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径   colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex1(file= r'E:\file.xlsx'):
    #从每一页的某一行开始
    colnameindex = 0

    #获得excel中的数据
    data = open_excel1(file)

    # 获取所有sheet页
    sheets = data.sheet_names()
    print(type(sheets), sheets)

    for index in range(0,len(sheets)):
        table = data.sheets()[index]
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        if nrows >0 and nrows > 0:
            colnames =  table.row_values(colnameindex) #某一行数据
            list =[]
            for rownum in range(1,nrows):

                 row = table.row_values(rownum)
                 if row:
                     app = {}
                     for i in range(len(colnames)):
                        app[colnames[i]] = row[i]
                     list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname1(file= r'E:\file.xlsx',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel1(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():
   tables = excel_table_byindex1()
   for row in tables:
       print(row)

   tables = excel_table_byname1()
   for row in tables:
       print(row)

if __name__=="__main__":
    main()