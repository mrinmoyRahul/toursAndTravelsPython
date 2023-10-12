#!C:\Python37-32\python.exe
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
i=cgi.FieldStorage()
ide=int(i.getvalue('a8'))
a=i.getvalue('a1')
b=i.getvalue('a2')
c=i.getvalue('a3')
e=i.getvalue('a4')
cur.execute("update packages set image='%s',name='%s',description='%s', per_head='%s' where pack_id=%d"%(a,b,c,e,ide))
print("location:package_up.py?msg=updated:\r\n\r\n")
db.commit()