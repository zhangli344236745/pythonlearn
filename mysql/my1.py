__author__ = '0138695'
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='test')

cursor = conn.cursor()
effect_row = cursor.execute("select * from user")
row_1 = cursor.fetchone()
conn.commit()
cursor.close()
conn.close()
print row_1