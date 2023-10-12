#!C:\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="admin")
cur=db.cursor()
cur.execute("select * from reg")
x=cur.fetchall()
print("""
<html>
<head>
<style>
table{
margin-top: 310px;
text-align:center;
background-color:#D5D8DC;
}
hr{
background-color:#AEB6BF;
height:5px;
}
ol {background-color:#E5E8E8;

	width: 1000px;
	height: 60px;
	margin-top:10px;
	
	}
ol li{
	background-color:#99A3A4;
	padding-top: 15px;

	width: 100px;
	height: 35px;
	padding-top: 15px;
	list-style-type: none;
	text-align: center;
	float:right;
	border-radius: 10px;
	margin-left: 10px;
    margin-top: 5px;
	
	
}

ol li a{
	color: #D5D8DC;
	text-decoration: none;
}
footer{
margin-top:100px;
background-color:#616A6B;
height:50px;
}
a{
color: #85929E;
	text-decoration: none;
}
</style>
</head>
<body bgcolor=#212F3D><center>
<ol>

<li><a href="#">Contact Us</a></li>
<li><a href="fetch.py">User Data</a></li>
<li><a href="#">Login/Register</a></li>
<li><a href="reg.html">Home</a></li>
</ol>
<hr><marquee style="background-color:#EAEDED;">user data</marquee></hr>
<hr>

</hr>
<table border=2>
<tr ><td>id</td><td>name</td><td>address</td><td>ph</td><td>pin</td><td>dob</td><td>pass</td><td>repass</td><td>delete</td><td>edit</td></tr>
""")
for i in x:

	print("""
	<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href="del.py?id=%d">delete</a></td><td><a href="edit.py?id=%d">edit</a></td></tr>
	"""%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0],i[0]))
print("""
</table></center>
<footer><p>rohit</p>
</footer>
</body>
</html>

""")