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

$sqlconstat = "SELECT vuilcontainerID FROM vuilcontainer, vuilcontainerStatus WHERE vuilcontainer.vuilcontainerID = vuilcontainerStatus.FK_vuilcontainerID";
$resultconstat = $conn->query($sqlconstat);

/*if ($resultcon->num_rows > 0) {
    // output data of each row
    while($row = $resultcon->fetch_assoc()) {
        echo "id: " . $row["vuilcontainerID"]. " - Grootte: " . $row["grootte"]. " - Locatie: " . $row["locatie"] . " \n";
    }
} else {
    echo "0 results";
}
$conn->close();*/

if($resultstat->num_rows > 0) {
    while($row = $resultstat->fetch_assoc()){
        echo "id: " . $row["FK_vuilcontainerID"] . " - Diepte (in percentages): " . $row["percentageDiepte"] . " - Diepte Afval (in CM): " . $row["diepteAfvalCM"] . " - Gewicht (in KG): " . $row["gewichtKG"] . " - Datum: " . $row["datum"] . " \n";
    }
} else {
    echo "0 results";
}
$conn->close();
?>