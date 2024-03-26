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

# Build the SQL Call (note that the initial value of ID will need to be changed if you wish to test this as it is a unique value)
newEntry = (2, "Shape", "Technique", "Painter", "Inscription", "Subject", "Collection", '1000-10-12', "BLOBLINK" )
itemQuery = "INSERT INTO Records (ID, Shape, Technique, Painter, Inscription, Subject, Collection, Date, Blob_Link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
cursor.execute(itemQuery, newEntry)

#Commit and Terminate SQL Server Connection
connection.commit()
cursor.close()
connection.close()

