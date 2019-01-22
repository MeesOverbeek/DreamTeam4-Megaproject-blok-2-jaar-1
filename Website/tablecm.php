<!DOCTYPE html>
<html>
<head>

<title>Ravensweerd - Alle vuilcontainers</title>
<link rel="stylesheet" type="text/css" href="index.css">
<meta http-equiv="refresh" content="15">
<link rel="shortcut icon" type="image/png" href="/favicon.png"/>

</head>
<body>

<?php /*
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

$sqlid = "SELECT * FROM vuilcontainerproject.vuilcontainerStatus GROUP BY FK_vuilcontainerID
ORDER BY LENGTH(FK_vuilcontainerID), FK_vuilcontainerID";
$resultid = $conn->query($sqlid);

$conn->close();
*/
?>

<div class="title">
<h1>Ravensweerd - Tabel</h1>
</div>
<ul>
  <li><a href="index.php">Dashboard</a></li>
  <li class="active">Alle vuilcontainers</li>
  <li><a href="volvuil.php">Bijna volle vuilcontainers</a></li>
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
        <td><a href="table.php">Vuilcontainer ID</a></td>
        <td><a href="tableper.php">Percentage vol</a></td>
        <td>Diepte afval in CM</td>
        <td><a href="tablekg.php">Gewicht in KG</a></td>
        <td><a href="tabledatum.php">Datum laatste meting</a></td>
    </thead>
    <tbody>

    </tbody>
</table>

<!--
<table id="myTable">
	
    id of <col> tags should be "col" + index of table(1 = first table, 2 = second table) + _ (underscore) + column index(1.2.3.4...)
    
	<colgroup>
		<col id="col1_1"></col>
		<col id="col1_2"></col>
		<col id="col1_3"></col>
        <col id="col1_4"></col>
        <col id="col1_5"></col>
    </colgroup>
    <div class="table">
	<thead>
		<tr>
            <?php /*
			echo "<td>Vuilcontainer ID</td>";
            echo "<td>Percentage vol</td>";
            echo "<td>Diepte afval in CM</td>";
			echo "<td>Gewicht in KG</td>";
            echo "<td>Datum laatste meting</td>";
            ?>
		</tr>
	</thead>
	<tbody>
    <?php
    $all_property = array();
    echo "<table class='data-table' id='myTable'>
    <tr class='data-heading'>";
    while($property = mysqli_fetch_field($resultstat)){
        array_push($all_property, $property->name);
    }
    echo "</tr>";

    echo "<div class='highlightedColumn'>";
    while($row = mysqli_fetch_array($resultstat)) {
        echo "<tr>";
        echo "<td>" . $row['FK_vuilcontainerID'] . "</td>";
        echo "<td>" . $row['percentageDiepte'] . "</td>";
        echo "<td>" . $row['diepteAfvalCM'] . "</td>";
        echo "<td>" . $row['gewichtKG'] . "</td>";
        echo "<td>" . $row['datum'] . "</td>";
        echo "</tr>";
    }
    echo "</div>";
    echo "</table>";
    */
    ?>
    </tbody>
</div>
</table>
<script type="text/javascript">
initSortTable('myTable', Array('S', 'N', 'N', 'N', 'S'));
</script>-->

</body>
</html>