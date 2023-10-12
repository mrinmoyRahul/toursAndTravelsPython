#!C:\Python37-32\python.exe
'''print("Content-type:text/html\r\n\r\n")'''
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
form=cgi.FieldStorage()
packageName=form.getvalue("packageName")
packageDescription=form.getvalue("packageDescription")
amountPerHead=int(form.getvalue("amountPerHead"))
cur.execute("insert into packages(name, description, per_head) values('%s','%s',%d)"%(packageName,packageDescription,amountPerHead))
db.commit()
print("location:packageUpload.html\r\n\r\n")