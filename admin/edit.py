#!C:\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
i=cgi.FieldStorage()
cusid=int(i.getvalue("id"))
cur.execute("select * from customer where cus_id=%d"%(cusid))
x=cur.fetchone()
print("""
<html>
<body>
<form action="edit_code.py">
<input type="text" name="a2" value="%s">
<input type="text" name="a3" value="%s">
<input type="text" name="a4" value="%s">
<input type="hidden" name="a8" value="%d">
<input type="submit">
</form>
</body>
</html>

"""%(x[1],x[2],x[3],x[0]))
