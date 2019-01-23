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
<p>Voor het AAI-gedeelte hebben we een algoritme geschreven dat berekent wat de beste dag is om de afvalcontainer te legen. <br>
Dit wordt berekend aan de hand van het percentage dat de prullenbak elke dag gevuld wordt. <br>
Het algoritme neemt van elke dag het percentage dat de container gevuld is en berekent op welke dag de prullenbak vol is. Dit kun je berekenen over zoveel weken als je wilt. <br>
Als van de hoeveelheid weken dat het algoritme berekend is op welke dag de container vol raakt wordt er berekent op welke dag de container gemiddeld vol raakt. <br>
Hieruit krijg je dan een dag in de week dat de container het beste geleegd kan worden. <br><br>
Omdat wij op geen data hadden van de prullenbakken die er nu staan hebben wij hier een oplossing op gemaakt. <br>
We hebben een stukje code gemaakt dat over de hoeveelheid weken dat je wilt data maakt. Dit doen we doormiddel van de Random functie. <br>
We hebben bepaald dat er rustige dagen, normale dagen en drukke dagen zijn. <br>
Op elke dag is er dan een maximaal percentage dat de prullenbak kan opvullen. <br>
Hierdoor kunnen we dus een simulatie draaien van zoveel weken als je wilt. <br><br>
Als voorbeeld:<br>
Rustige dagen: max 15%, normale dagen: max 30%, drukke dagen: max 40%. <br>
Als we dan 100.000 weken simuleren (1923 jaar) geeft het algoritme aan dat de beste dag om het afval te legen vrijdag is. <br>
Dan zit de prullenbak gemiddeld voor 107% vol. <br>
Dit betekend dus dat de prullenbak vrijdag vroeg op de dag geleegd moet worden zodat die niet overvol raakt, 
maar als dit vroeg gebeurd zit de container dus net niet vol. 
</p> 

</body>
</html>
