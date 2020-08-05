import sqlite3

conn = sqlite3.connect('students.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE student
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50));''')
conn.execute("INSERT INTO student (ID,NAME,AGE,ADDRESS) \
      VALUES (1, 'Paul', 32, 'California')")

conn.execute("INSERT INTO student (ID,NAME,AGE,ADDRESS) \
      VALUES (2, 'Allen', 25, 'Texas')")

conn.execute("INSERT INTO student(ID,NAME,AGE,ADDRESS) \
      VALUES (3, 'Teddy', 23, 'Norway')")

conn.execute("INSERT INTO student (ID,NAME,AGE,ADDRESS) \
      VALUES (4, 'Mark', 25, 'Rich-Mond')")

conn.commit()

cursor = conn.execute("SELECT id, name, age, address from student")
for row in cursor:
    print(row)
conn.close()
