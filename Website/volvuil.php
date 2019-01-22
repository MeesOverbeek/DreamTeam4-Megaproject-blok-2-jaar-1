<!DOCTYPE html>
<html lang="en">
<head>
  <title>Ravensweerd - Bijna volle vuilcontainers</title>
  <link rel="stylesheet" type="text/css" href="index.css?v=1.1">
  <meta http-equiv="refresh" content="15">
  <link rel="shortcut icon" type="image/png" href="/favicon.png"/>
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

$sqlvol = "SELECT * FROM vuilcontainerStatus WHERE percentageDiepte > 79";
$resultvol = $conn->query($sqlvol);

$sqlvoor = "SELECT * FROM vuilcontainerVoorspelling";
$resultvoor = $conn->query($sqlvoor);

$conn->close();

?>

<div class="title">
<h1>Ravensweerd - Bijna volle vuilcontainers</h1>
</div>
<ul>
  <li><a href="index.php">Dashboard</a></li>
  <li><a href="table.php">Alle vuilcontainers</a></li>
  <li class="active">Bijna volle vuilcontainers</li>
</ul>
<br>

<h3>Vandaag is het</h3>
<p>
  <?php
    echo date("d M Y - H:i");
  ?>
</p> 

</body>
</html>