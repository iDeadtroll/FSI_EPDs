import sqlite3
import csv

#Crear conexión
conn = sqlite3.connect('mydatabase.db')

#Obtener cursor
cursor = conn.cursor()

#Ejecutar sentencia de creacioón de tabla

f=open('14_FootballClubs.csv','r')
next(f,None)
reader = csv.reader(f, delimiter = ',')

for row in reader:
    cursor.execute("INSERT or IGNORE INTO Clubs VALUES (?,?,?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
conn.commit()
cursor.execute('SELECT Club_Name FROM Clubs WHERE Market_Value_Of_Club >= Average_Market_Value_of_Players And ID <= 5')
rows= cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('UPDATE Clubs SET Squad_Size = 25   WHERE Average_Age_Of_Players>=28 ')
conn.commit()
cursor.execute('SELECT MAX(Market_Value_Of_Club) FROM Clubs')
rows= cursor.fetchall()
print(rows)