import mysql.connector as conn

#new connection with seerver
#change host, user, password
server = conn.connect(host = "localhost", user="root", password="123qwe") #local server

cursor = server.cursor()
print('connected')

#create database
def createDB(dbname):
    print('creted')
    cursor.execute("CREATE DATABASE gym")
    return cursor

#delete database
def deleteDB(dbname):
    print('dropped')
    cursor.execute("DROP DATABASE gym")
    print('ok')
    return

#list with sql commands from file
def sql(cursor, file):
    print('ok')
    with open(file, 'r', encoding="utf-8") as f:
        sql = f.read()
        f.close()
    return sql.split(';')

#insert data into database from file
def insertData(dbname):
    print('ok')
    #change host, user, password
    db = conn.connect(host = "localhost", user="root", password="123qwe", database = dbname)
    cursor = db.cursor()
    sqlcommands = sql(cursor, 'data.sql')
    
    for com in sqlcommands:
        cursor.execute(com.replace('\n', ' '))
        db.commit()
    return


def main():
    dbname = 'gym'
    try:
        deleteDB(dbname)
    except:
        print("database does not exist, to be deleted or something else went wrong")
    finally:
        print("connected")
    try:
        createDB(dbname)
    except :
        print("something wrong")
    else:
        print("database created")
    try:
        insertData(dbname)
    except Exception as e:
        print("data couldn't insert into database")
        print(e)
    else:
        print("data inserted succesfully")
    return

main()
