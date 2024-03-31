import mysql.connector


def conData():

    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="",
        database="workout",

       

    )
    cursor = mydb.cursor()
    return cursor, mydb
        
    


