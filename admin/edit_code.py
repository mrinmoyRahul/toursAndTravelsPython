#!C:\Python37-32\python.exe
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="travel")
cur=db.cursor()
i=cgi.FieldStorage()
ide=int(i.getvalue('a8'))
b=i.getvalue('a2')
c=i.getvalue('a3')
e=i.getvalue('a4')
cur.execute("update customer set name='%s',email='%s',password='%s' where cus_id=%d"%(b,c,e,ide))
print("location:user_dt.py?msg=updated:\r\n\r\n")
db.commit()