#!C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
d=cgi.FieldStorage()
id=int(d.getvalue('id'))
cur.execute("select * from packages where id=%d"%(id))
x=cur.fetchone()
print("""
<html>
<body>
	<input type="text" value="%s" name="nameOfPackage">
	<input type="text" value="%s" name="description">"""%(x[2],x[3]))
	
print("""</body>
</html>
""")
