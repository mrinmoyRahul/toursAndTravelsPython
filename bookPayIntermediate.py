#!C:\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
d=cgi.FieldStorage()
nop=int(d.getvalue('noOfPeople'))
a=int(d.getvalue('id'))
cur.execute("select * from packages where pack_id=%d"%(a))
x=cur.fetchone()
sum=nop*x[4]
print('''<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
	<link rel="stylesheet" href="CSS/bookPayIntermediate.css">
    <link href="https://fonts.googleapis.com/css?family=Dancing+Script" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
	<title>Minimum Bootstrap HTML Skeleton</title>
	<title>Minimum Bootstrap HTML Skeleton</title>
	<style>
        
img{
    height:554px;
    width:660px;
}
.col{
	padding: 0px;
    
}
.sec
{
    padding:0px;
	
	background-color: #3895d3;
}
.frame{
   margin-top:100px;
   margin-left:100px;
}
label
{
	//margin-top:50px;
	//margin-bottom:50px;
	margin-right:50px;
	font-family: 'Roboto', sans-serif;
}
input[type="text"]{
	width:50px;
}
button
{
    bottom:5px;
    position:absolute;
    margin-left:150px;
}
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
.footer
 {
     background-color:#2096ba;
     
    bottom:0px;
     position:static;
    height:100px;  
       
 }
 .footer-text
        {
            padding-top: 40px;
            text-align:center;
        }



    </style>
	<!--  -->

	

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
<div class="row">
    <div class="col">
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="images/beach.jpeg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="images/mountains.jpeg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="images/sea.jpeg" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    </div>
    <div class="col sec">''')

print('''
<div class="frame"><form action=bookPayIntermediate.py>

<label><h3>Amount per head:</h3></label><label><h3>%d</h3></label>'''%(x[4]))
print('''
<input type='hidden' name='id' value=%d>
</label><br>
<label><h3>No. of people:</h3></label><input type='text' name='noOfPeople' value=%d><br>
<label><h3>Total:</h3></label><label><h3>%d</h3></label><br>'''%(a,nop,sum))
print('''
<input type="submit">
<button>pay</button>
</form>
</div>
</div>
</div>
<div class="footer">
        <p class="footer-text">copyright @ Ardent Computech pvt. Ltd</p>
    </div>

	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>

	<script>
	</script>

	<script>
	</script>

</body>

</html>''')
