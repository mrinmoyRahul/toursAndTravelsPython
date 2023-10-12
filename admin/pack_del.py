#!C:\Python37-32\python.exe
'''print("Content-type:text/html\r\n\r\n")'''
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
de=cgi.FieldStorage()
i=int(de.getvalue("id"))
cur.execute("delete from packages where pack_id=%d"%(i))

db.commit()
print("location:package_up.py\r\n\r\n")