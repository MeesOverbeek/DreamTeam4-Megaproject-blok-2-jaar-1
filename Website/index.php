<!DOCTYPE html>
<html lang="en">
<head>
  <title>Ravensweerd</title>
  <link rel="stylesheet" href="database.php">
  <link rel="stylesheet" type="text/css" href="index.css">
</head>
<body>

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

$conn->close();
?>

<h1>Ravensweerd</h1>
<ul class="nav nav-pills nav-stacked">
  <li class="active"><a href="#section1">Dashboard</a></li>
  <li><a href="#section2">Age</a></li>
  <li><a href="#section3">Gender</a></li>
  <li><a href="#section3">Geo</a></li>
</ul>
<br>
<br>
    
<h4>Aantal vuilcontainers</h4>
<p>
  <?php
    echo $resultcon->num_rows;
  ?>
</p>

<h4>Totaal gewicht in KG</h4>
<p>
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

<h4>Pages</h4>
<p>100 Million</p> 

<h4>Sessions</h4>
<p>10 Million</p> 

<h4>Bounce</h4>
<p>30%</p>

<p>Text</p>
<p>Text</p> 

<?php
  $all_property = array();
  echo "<table class='data-table'>
  <tr class='data-heading'>";
  while($property = mysqli_fetch_field($resultstat)){
    echo "<td>" . $property->name . "</td>";
    array_push($all_property, $property->name);
  }
  echo "</tr>";

  while($row = mysqli_fetch_array($resultstat)) {
    echo "<tr>";
    foreach ($all_property as $item) {
      echo "<td>" . $row[$item] . "</td>";
    }
    echo "</tr>";
  }
  echo "</table>";
?>

</body>
</html>
