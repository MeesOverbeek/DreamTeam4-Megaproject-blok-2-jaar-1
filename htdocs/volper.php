<!DOCTYPE html>
<html>
<head>

<title>Ravensweerd - Bijna volle vuilcontainers</title>
<link rel="stylesheet" type="text/css" href="index.css">
<meta http-equiv="refresh" content="15">
<link rel="shortcut icon" type="image/png" href="/favicon.png"/>

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

//Zorgt ervoor dat alleen de containers die bijna vol zijn met de laatste meting geselecteerd worden en sorteert op hoe vol een container is
$sqlid = "SELECT * FROM vuilcontainerproject.vuilcontainerStatus 
WHERE percentageDiepte > 79
AND datum = (SELECT MAX(datum) FROM vuilcontainerStatus WHERE FK_vuilcontainerID = FK_vuilcontainerID)
GROUP BY FK_vuilcontainerID
ORDER BY percentageDiepte DESC";
$resultid = $conn->query($sqlid);

$conn->close();
?>

<div class="title">
<h1>Ravensweerd - Tabel</h1>
</div>
<!--Maakt een lijst van de drie hoofdpagina's met links-->
<ul>
  <li><a href="index.php">Dashboard</a></li>
  <li><a href="table.php">Alle vuilcontainers</a></li>
  <li>Bijna volle vuilcontainers</li>
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

<!--Maakt een tabel-->
<table>
    <thead>
        <td><a href="volvuil.php">Vuilcontainer ID</a></td>
        <td>Percentage vol</td>
        <td><a href="volcm.php">Diepte afval in CM</a></td>
        <td><a href="volkg.php">Gewicht in KG</a></td>
        <td><a href="voldatum.php">Datum laatste meting</a></td>
    </thead>
    <tbody>
        <!--Haalt de nodige informatie uit de database en stopt het in rijen-->
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