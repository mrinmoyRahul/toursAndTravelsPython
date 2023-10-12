#!C:\Python37-32\python.exe
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="travel")
cur=db.cursor()
form=cgi.FieldStorage()
username=form.getvalue("a1")
password=form.getvalue("a2")
cur.execute("select * from admin")
x=cur.fetchall()
c=0
for i in x:
    if i[1]==username and i[2]==password:
        c=1
        break
if c==0:
    print("location:index.html?msg=notdone\r\n\r\n")		
else:
    print("location:dashboard.html\r\n\r\n")