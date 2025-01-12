import mysql.connector 
import pandas as pd
import numpy as np


mydb=mysql.connector.connect(
     host="127.0.0.1",
     port="3306",
     user="root",
     password="2389"
)
cur=mydb.cursor()

try:
    cur.execute("create database mydb")

except:
    mydb.rollback()

cur.execute("show databases")

mydb1=mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="2389",
    database="mydb"
)

cur1=mydb1.cursor()
try:
    cur1.execute("create table mobile ( id int primary key, "
                + "name varchar(100), "
                + "price int, "
                + "sold int, "
                + "rating_evaluate float)")
except:
    mydb1.rollback()

url=r"E:\PTIT\python\transform\device_mobile.csv"
df=pd.read_csv(url)

df.columns=['stt','id','name','price','sold','rating_evaluate']
df1=df.fillna(0)
df1['sold']=df1['sold'].astype(int)


'''for _, row in df1.iterrows():
    value = (row['id'], row['name'], row['price'], row['sold'], row['rating_evaluate']) 
    try:
        cur1.executemany("INSERT INTO mobile (id,name,price,sold,rating_evaluate) VALUES (%s,%s,%s,%s,%s)",value)
    except:
        mydb1.rollback()
'''
cur1.execute("select * from mobile")

result= cur1.fetchall()
print(mydb1)

print(df1.shape[0])





