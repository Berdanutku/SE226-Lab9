import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user= "root",
    passwd= "" )
cursorObject= database.cursor()
cursorObject.execute("DROP DATABASE Marvel")

cursorObject.execute("CREATE DATABASE Marvel")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database = 'Marvel',
    passwd="" )
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to the MySQL server", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database() ")
    record = cursor.fetchone()
    print("Connected to the database", record)

try:
    connection = mysql.connector.connect(
        host="localhost",
        database="Marvel",
        user="root",
        password="" )
    mysqlQuery = """
     CREATE TABLE Marvel(
     ID int(30) NOT NULL,
     MOVIE varchar(30) NOT NULL,
     DATE varchar(30) NOT NULL,
     MCUPHASE varchar(30)
     PRIMARY KEY(ID))"""

    cursor = connection.cursor()
    result = cursor.execute(mysqlQuery)

    cursor.execute("SHOW TABLES")
    for tableName in cursor:
        print(tableName)
except mysql.connector.Error as error:
    print("Fail!",error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL is closed")

file = open("Marvel.txt")

try:
    connection = mysql.connector.connect(
        host="localhost",
        database="Marvel",
        user="root",
        password=""
    )
    CursorObject = connection.cursor()
    while file:
        i = file.readline()
        if i == "":
            break
        a = text.split()
        Insert = """INSERT INTO marvel (ID, MOVIE, DATE, MCU_PHASE)
                 VALUES (%s, %s, %s, %s)"""
        record = (a[0], a[1], a[2], a[3])
        CursorObject.execute(Insert, record)
        connection.commit()
    print("Records are added into table.")
    CursorObject.close()

    sql1 = "SELECT MOVIE FROM marvel"
    cursorObject = connection.cursor()
    cursorObject.execute(sql1)
    record = cursorObject.fetchall()
    for x in record:
        print(x)

    sql2 = "DELETE FROM marvel WHERE MOVIE= 'TheIncredibleHulk'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql2)
    connection.commit()

    sql3 = "SELECT * FROM marvel WHERE MCU_PHASE='Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql3)
    record2 = cursorObject.fetchall()
    for x in record2:
        print(x)

    sql4 = "UPDATE marvel SET DATE= 'November 3, 2017' WHERE MOVIE='Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql4)
    connection.commit()

except mysql.connector.Error as error:
    print("Fail!",error)

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed.")