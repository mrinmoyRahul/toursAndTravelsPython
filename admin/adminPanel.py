#!C:\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
form=cgi.FieldStorage()
a=form.getvalue("a1")
b=form.getvalue("a2")
cur.execute("insert into packages (name,description) values('%s','%s')"%(a,b))
db.commit()

