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

$sqlconstat = "SELECT vuilcontainerID FROM vuilcontainer, vuilcontainerStatus 
               WHERE vuilcontainer.vuilcontainerID = vuilcontainerStatus.FK_vuilcontainerID";
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

/*if($resultstat->num_rows > 0) {
    while($row = $resultstat->fetch_assoc()){
        echo "id: " . $row["FK_vuilcontainerID"] . " - Diepte (in percentages): " . $row["percentageDiepte"] . " - Diepte Afval (in CM): " . $row["diepteAfvalCM"] . " - Gewicht (in KG): " . $row["gewichtKG"] . " - Datum: " . $row["datum"] . " \n";
    }
} else {
    echo "0 results";
}
$conn->close();*/

/*$sqlrecent = "SELECT * FROM vuilcontainerStatus t 
    INNER JOIN (
    SELECT FK_vuilcontainerID, max(datum) AS MaxDate
    FROM vuilcontainerStatus
    GROUP BY FK_vuilcontainerID
) tm ON t.FK_vuilcontainerID = tm.FK_vuilcontainerID AND t.datum = tm.MaxDate";

$resultrecent = $conn->query($sqlrecent);

if($resultrecent->num_rows > 0){
    while($row = $resultrecent->fetch_assoc()){
        echo "Id: " . $row[FK_vuilcontainerID] . " - Datum: " . $row[MaxDate] . " \n";
    }
} else {
    echo "0 results";
}
$conn->close();*/
echo "<tr>
<th> Vuilcontainer ID </th>
<th> Vuilcontainer vol (in %) </th>
<th> Gewicht (in KG) </th>
<th> Datum meting </th>
</tr>";

if($resultstat->num_rows > 0) {
while($row = mysqli_fetch_array($resultstat))
{
echo "<tr>";
echo "<td>" . $row["FK_vuilcontainerID"] . "</td>";
echo "<td>" . $row["percentageDiepte"] . "</td>";
echo "<td>" . $row["gewichtKG"] . "</td>";
echo "<td>" . $row["datum"] . "</td>";
echo "</tr>";
}
}else{
echo "0 results";
}; 
?>