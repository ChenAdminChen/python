import xlrd
import MySQLdb
import argparse
import  datetime

#获得excel表信息
def open_excel(file):
    try:
        data =  xlrd.open_workbook(file)
    except Exception as e:
        print(str(e))
    return data

def excel_table_byindex(file):
    # 从每一页的某一行开始
    colnameindex = 2

    #数据集
    list = []

    #获得excel表数据
    data = open_excel(file)

    # 获取所有sheet页
    sheets = data.sheet_names()

    for index in range(len(sheets)):

        #获得具体数据
        table = data.sheets()[index]
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数

        if nrows > 2 and ncols > 0:
            #获得一行数据
            colnames = table.row_values(0)

            org = 0
            device_id = 0

            #循环行
            for rownum in range(colnameindex, nrows):

                #获得数据
                row = table.row_values(rownum)

                if row:
                    app = {}

                    #循环列
                    for i in range(len(colnames)):

                        if colnames[i] == 'device_did' and row[i] != '':
                            did = row[i]
                            args = get_device_and_org_info(did)

                            org = args["org"]
                            device_id = args["device_id"]

                        if colnames[i] == 'code' and row[i] == '':
                            break

                        if row[i] == '' or row[i] is '':
                            app[colnames[i]] = None
                        else:

                            #12.0 ---12  12.4---123
                            if type(row[i]) == float:

                                if row[i] == int(row[i]):
                                    app[colnames[i]] = int(row[i])

                                else:
                                    app[colnames[i]] = float(row[i])
                            else:
                                app[colnames[i]] = row[i]

                    if 'code' in app:

                        app['owner'] = int(org)
                        app["device_id"] = int(device_id)

                        list.append(app)

    return list


def main(file):

    tables = excel_table_byindex(file)

    name = list(tables[0].keys())

    name_data = name[4:-1]

    sql_name = 'insert into user_index (' + ','.join(name_data) + ') values(%s' + ',%s' * (len(name_data) - 1) + ")"


    cursor = connection.cursor()
    for row in tables:
        try:
            row_data = []
            for n in name_data:
                row_data.append(row[n])

            result_index = cursor.execute(sql_name,row_data)

            if result_index >0:

                id = cursor.lastrowid

                sql_device_channel = "INSERT INTO device_channel (device_id, index_code, index_id) values(%s, %s, %s)"

                result = cursor.execute(sql_device_channel,[row['device_id'],row['code'],id])

                if result>0:
                    print('成功')
                else:
                    print('不成功')
            else:
                print('不成功')

        except Exception as e:
            #cursor.connection.rollback()
            print(str(e))
            continue

    cursor.connection.commit()

    cursor.close()

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='file_address root password ip db')

    parser.add_argument('file', metavar = 'N', type = str, nargs = '+', help = 'an file for the progarm')
    parser.add_argument('root', metavar = 'N', type = str, nargs = '+', help = 'mysql user name')
    parser.add_argument('passwd', metavar = 'N', type = str, nargs = '+', help = 'mysql user password')
    parser.add_argument('ip', metavar = 'N', type = str, nargs = '+', help = 'ip address')
    parser.add_argument('db', metavar = 'N', type = str, nargs = '+', help = 'database name')

    args = parser.parse_args()

    root = args.root[0]

    passwd = args.passwd[0]

    ip = args.ip[0]

    db = args.db[0]

    try:
        connection = MySQLdb.connect(user = root, passwd = passwd, host = ip, db=db, charset="utf8")
    except:
        print("Could not connect to MySQL server.")
        exit(0)

    print(args.file[0], args.root[0], args.passwd[0], args.ip[0], args.db[0])

    start = datetime.datetime.now()
    main(args.file[0])
    end = datetime.datetime.now()
    print(end-start)






