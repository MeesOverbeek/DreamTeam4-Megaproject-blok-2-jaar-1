<!DOCTYPE html>
<html lang="en">
<head>
  <title>Ravensweerd - Dashboard</title>
  <link rel="stylesheet" type="text/css" href="index.css?v=1.1">
  <link rel="shortcut icon" type="image/png" href="/favicon.png"/>
  <meta http-equiv="refresh" content="15">
</head>

<body>

<!--Verbindt de website met de database en haalt er informatie uit-->
<?php 
$servername = "10.0.0.210";
$username = "sensor";
$password = "buitenbankje123";
$dbname = "vuilcontainerproject";

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

error_reporting(E_ALL);
ini_set('display_errors', 1);

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sqlcon = "SELECT * FROM vuilcontainer";
$resultcon = $conn->query($sqlcon);

$sqlstat = "SELECT * FROM vuilcontainerStatus";
$resultstat = $conn->query($sqlstat);

$sqlvoor = "SELECT * FROM vuilcontainerVoorspelling";
$resultvoor = $conn->query($sqlvoor);

$sqlid = "SELECT vuilcontainerID FROM vuilcontainer";
$resultid = $conn-> query($sqlid);



$conn->close();
?>

<div class="title">
<h1>Ravensweerd - Dashboard</h1>
</div>
<!--Maakt een lijst van de drie hoofdpagina's met links-->
<ul>
  <li class="active">Dashboard</li>
  <li><a href="table.php">Alle vuilcontainers</a></li>
  <li><a href="volvuil.php">Bijna volle vuilcontainers</a></li>
</ul>
<br>
   
<h3>Vandaag is het</h3>
<p>
  <!--Vertelt de huidige tijd-->
  <?php
    echo date("d M Y - H:i");
  ?>
</p> 
<br>
<br>
    <h3>Aantal vuilcontainers</h3>
    <p>
      <!--Telt hoeveel UNIEKE vuilcontainers er zijn volgens het tabel vuilcontainers in de database-->
      <?php
      $listid = array();
      while($row=mysqli_fetch_assoc($resultid)){
          $listid[] = $row;
      }
        echo count($listid)
      ?>
    </p>
    <br>
    
    <h3>Totaal gewicht in KG</h3>
    <p>
      <!--Telt het gewicht op van alle vuilcontainers bij elkaar-->
      <?php
        $totaalGewicht = 0;
        if($resultstat->num_rows > 0) {
          while($row = $resultstat->fetch_assoc()){
            $totaalGewicht = $totaalGewicht + $row["gewichtKG"];
          }
          echo $totaalGewicht;
        } else {
          echo "Geen prullenbakken beschikbaar";
        }
      ?>
    </p> 
    <br>

<h3>Uitleg AI Expert</h3>
<p></p> 
<br>

</body>
</html>
