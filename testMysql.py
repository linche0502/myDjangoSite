import pymysql

def dbC(command):
    conn= pymysql.connect(host= "localhost", port= 3306, user= "root", passwd= "01234567", charset= "utf8", db= "testdb")
    with conn.cursor() as cursor:
        cursor.execute(command)
        data= cursor.fetchall()
        conn.commit()
    conn.close()
    return data

# 建立Table
# dbC('''
#     CREATE TABLE IF NOT EXISTS TESTBOOK(
#         ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         Title VARCHAR(100) NOT NULL,
#         Author VARCHAR(40) NOT NULL,
#         date DATE
#     );
# ''')

# 插入資料
# for i in [["PHP","ME",'"2023-08-09"'], ["JAVA", "HE", '"2023-08-08"'], ["C", "UNKNOW", 'NOW()']]:
#     dbC(f'INSERT INTO TESTBOOK (Title, Author, Date) VALUES ("{i[0]}", "{i[1]}", {i[2]});')

# data= {"Title": value1, "Author": value2}
def insertDB(data):
    cols= ",".join(data.keys())
    values= ",".join(['"'+char+'"' for char in data.values()])
    dbC('INSERT INTO TESTBOOK ({}) VALUES ({})'.format(",".join(data.keys()), ",".join([f'"{char}"' for char in data.values()])))

# insertDB({"Title":"DJANGO", "Author":"ME", "Date":"2023-08-01"})


# 讀取資料
for row in dbC('SELECT * FROM TESTBOOK'):
    print(row)

print(dbC('SELECT author ,COUNT(*) FROM TESTBOOK GROUP BY author'))

print('finished')