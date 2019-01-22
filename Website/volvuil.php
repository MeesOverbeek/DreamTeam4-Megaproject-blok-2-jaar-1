<!DOCTYPE html>
<html>
<head>

<title>Ravensweerd - Alle vuilcontainers</title>
<link rel="stylesheet" type="text/css" href="index.css">
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

$sqlvoor = "SELECT * FROM vuilcontainerVoorspelling";
$resultvoor = $conn->query($sqlvoor);

$sqlid = "SELECT * FROM vuilcontainerproject.vuilcontainerStatus 
WHERE percentageDiepte > 79
AND datum = (SELECT MAX(datum) FROM vuilcontainerStatus WHERE FK_vuilcontainerID = FK_vuilcontainerID)
GROUP BY FK_vuilcontainerID
ORDER BY LENGTH(FK_vuilcontainerID), FK_vuilcontainerID";
$resultid = $conn->query($sqlid);

$conn->close();
?>

<div class="title">
<h1>Ravensweerd - Tabel</h1>
</div>
<ul>
  <li><a href="index.php">Dashboard</a></li>
  <li><a href="table.php">Alle vuilcontainers</a></li>
  <li>Bijna volle vuilcontainers</li>
</ul>
<br>

<h3>Vandaag is het</h3>
<p>
  <?php
    echo date("d M Y - H:i");
  ?>
</p> 
<br>
<br>

<table>
    <thead>
        <td>Vuilcontainer ID</td>
        <td><a href="tableper.php">Percentage vol</a></td>
        <td><a href="tablecm.php">Diepte afval in CM</a></td>
        <td><a href="tablekg.php">Gewicht in KG</a></td>
        <td><a href="tabledatum.php">Datum laatste meting</a></td>
    </thead>
    <tbody>
        <?php
            while($row = mysqli_fetch_array($resultid)) {
                echo "<tr>";
                echo "<td>" . $row['FK_vuilcontainerID'] . "</td>";
                echo "<td>" . $row['percentageDiepte'] . "</td>";
                echo "<td>" . $row['diepteAfvalCM'] . "</td>";
                echo "<td>" . $row['gewichtKG'] . "</td>";
                echo "<td>" . $row['datum'] . "</td>";
                echo "</tr>";
            }
        ?>
    </tbody>
</table>

</body>
</html>