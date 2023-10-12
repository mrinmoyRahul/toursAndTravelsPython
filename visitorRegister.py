#!C:\Python37-32\python.exe
'''print("Content-type:text/html\r\n\r\n")'''
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
form=cgi.FieldStorage()
name=form.getvalue("name")
email=form.getvalue("email")
pwd=form.getvalue("pwd")
cur.execute("insert into customer(name, email, password) values('%s','%s','%s')"%(name,email,pwd))
db.commit()
print("location:visitorRegister.html\r\n\r\n")