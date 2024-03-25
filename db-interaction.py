# ensure youre run the command "pip install pyodbc" for this to work
import pyodbc

server = 'trendal1.database.windows.net'
database= 'Beige'
username= 'trendal'
password= 'latrobe2024!'

# Establishing a connection to the SQL Server
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)

cursor = connection.cursor()


newEntry = (2, "Shape", "Technique", "Painter", "Inscription", "Subject", "Collection", '1000-10-12', "BLOBLINK" )

itemQuery = "INSERT INTO Records (ID, Shape, Technique, Painter, Inscription, Subject, Collection, Date, Blob_Link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.execute(itemQuery, newEntry)

connection.commit()

# Example fetch query
query = "SELECT * FROM Records"
cursor.execute(query)

cursor.close()
connection.close()

