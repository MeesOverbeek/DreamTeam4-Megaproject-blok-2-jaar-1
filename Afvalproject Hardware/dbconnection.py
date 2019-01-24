import MySQLdb
import datetime

#SETUP
db=MySQLdb.connect(host="10.0.0.210",user="sensor",
                  passwd="buitenbankje123",db="vuilcontainerproject")
cursor = db.cursor()

#FUNCTIE
def INSERT_SQL(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum):
    sql = "INSERT INTO vuilcontainerStatus(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum))

#VOORBEELD
try:
	INSERT_SQL("VC69", 10, 30, 50,"2007-05-08 12:35:29.123")
	db.commit()
except:
	db.rollback

db.close()
