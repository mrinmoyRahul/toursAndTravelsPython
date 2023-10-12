#!C:\Python37-32\python.exe
'''print("Content-type:text/html\r\n\r\n")'''
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
form=cgi.FieldStorage()
name=form.getvalue("name")
pwd=form.getvalue("pwd")
cur.execute("select * from customer")
x=cur.fetchall()
c=0
for i in x:
    if i[1]==name and i[3]==pwd:
        print("location:index.py\r\n\r\n")
        c=1
        break
if c==0:
    print("location:visitorLogin.html\r\n\r\n")