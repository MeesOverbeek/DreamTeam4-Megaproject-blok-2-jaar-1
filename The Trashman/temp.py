cursor.execute(
        "select * from vuilcontainerproject.vuilcontainerStatus group by FK_vuilcontainerID order by LENGTH(FK_vuilcontainerID), FK_vuilcontainerID;")


cursor.execute(
        "select * from vuilcontainerproject.vuilcontainerStatus where datum = (select max(datum) "
        "from vuilcontainerproject.vuilcontainerStatus where vuilcontainerStatus.FK_vuilcontainerID = FK_vuilcontainerID) "
        "group by FK_vuilcontainerID order by LENGTH(FK_vuilcontainerID), FK_vuilcontainerID;")