import sqlite3 as s3
import pandas as pd
print('Please Fill The Given Form')

name = str(input('Enter Your name : '))

age = int(input('Enter Your age : '))

phone = int(str(input('Enter your Phone Number : ')))

con = s3.connect('student.db' , timeout=10)
cur = con.cursor()
data = [(1,name , age , phone)]

sql = '''insert into studennt values (?,?,?,?)'''

#res = cur.execute(create_table) 

res1 = cur.executemany(sql , data)


res3 = '''select * from studennt'''

res4 = cur.execute(res3)

res_final = cur.fetchall()

res = pd.DataFrame([res_final])

print(res)


con.commit()

con.close()

