<?php
$id=$_GET['id'];
if(!isset($_GET['id'])){$id = 'Homepage';}
?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>Hurricane Hackers</title>
      <link rel="stylesheet" href="css/master.css">
      <script type="text/javascript" charset="utf-8" src="js/jquery-1.8.2.min.js"></script>     
      <script type="text/javascript" charset="utf-8">
	$(document).ready(function(){

	});
      </script>
</head>
<body>
<div id="wrapper">
<div id="header">
</div>
	</strong>
		<div class="buttons">
				<a href="http://hurricanehackers.com/">
					<div id="about">
					<p>&nbsp;<p>
					<p>&nbsp;<p>
					<p>about<p>
					</div>
				</a>
				<a href="https://github.com/hurricanehackers">
					<div id="git">
					<p>&nbsp;<p>
					<p>&nbsp;<p>
					<p>github<p>
					</div>
				</a>   
				<a href="#" target="_blank">
					<div id="wiki">
					<p>&nbsp;<p>
					<p>&nbsp;<p>
					<p>Wiki<p>
					</div>
				</a>  
				<a href="https://twitter.com/HurricaneH4x0rs" target="_blank">
					<div id="twitter">
					<p>&nbsp;<p>
					<p>&nbsp;<p>
					<p>@HurricaneH4x0rs<p>
					</div>
				</a>
		</div>
	<p>&nbsp;</p>
	<?php include_once("php/$id.php");?>
</div>
</body>
</html>                               
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    

