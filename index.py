#!C:\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("select * from packages")
x=cur.fetchall()
print('''<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
	<link rel="stylesheet" href="CSS/index.css">
    <link href="https://fonts.googleapis.com/css?family=Dancing+Script" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Shadows+Into+Light" rel="stylesheet">
	<title>Minimum Bootstrap HTML Skeleton</title>
    

	<!--  -->

	<style>
        .navbar
        {
            background-color:aquamarine;
            border-radius:5px;
            
        }
        .title
        {
            padding-right:180px;
            font-family: 'Dancing Script', cursive;
        
            
        }
        body
        {
            background: url("images/beach.jpg") no-repeat center center fixed;
            background-size: cover;
        }
        .footer
        {
            background-color:#2096ba;
            bottom:0px;
            width:100%;
            position:static;
            height:100px;
        }
        .footer-text
        {
            padding-top: 40px;
            text-align:center;
        }
        .heading
        {
            font-family: 'Shadows Into Light', cursive;
            text-align:center;
            margin-bottom:0px;
            padding-bottom:0px;
        }
        .row .col-sm >a >img
        {
            border-radius: 20px;
            border:2px solid blue;
        }
	</style>

</head>

<body>
	<ul class="nav justify-content-end navbar">
    <h1 class="title"><b>Never Ending Footsteps</b><i class="fas fa-shoe-prints"></i></h1>
  
  <li class="nav-item">
    <a class="nav-link" href="index.py">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">About Us</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Contact Us</a>
  </li>
</ul>
<h1 class="heading"><u>Our Packages</u></h1>
''')

no_of_records=len(x)
rows=int(no_of_records/4)
last_row=no_of_records%4
c=0
if no_of_records >=4:
	for j in range(rows):
		print('''<div class="row">''')
		for i in range(4):
			print('''<div class="col-sm"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>'''%(x[c][0],x[c][2]))
			c=c+1
		print('''</div>''')
if last_row==1:
	print('''<div class="row">
	<div class="col-sm"></div>
	<div class="col-sm one"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>
	<div class="col-sm"></div>
	</div>'''%(x[c][0],x[c][2]))
if last_row==2:
	print('''<div class="row">
	<div class="col-sm"></div>
	<div class="col-sm"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>'''%(x[c][0],x[c][2]))
	c=c+1
	print('''<div class="col-sm"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>
	<div class="col-sm"></div>
	</div>'''%(x[c][0],x[c][2]))	
if last_row==3:
	print('''<div class="row">
	<div class="col-sm"></div>
	<div class="col-sm three"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>'''%(x[c][0],x[c][2]))
	c=c+1
	print('''<div class="col-sm three"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>'''%(x[c][0],x[c][2]))
	c=c+1
	print('''<div class="col-sm three"><a href="packageDescription.py?id=%s"><img src="images/scenery.jpeg"></a><h5>%s</h5></div>
	<div class="col-sm"></div>
	</div>'''%(x[c][0],x[c][2]))


print('''
    <div class="footer">
        <p class="footer-text">copyright @ Ardent Computech pvt. Ltd</p>
    </div>
    
    
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>

	<script>
	</script>

</body>

</html>''')
