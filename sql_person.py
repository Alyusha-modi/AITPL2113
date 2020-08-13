import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table Alyusha_person(name varchar(10),dob DATE,address varchar(50),pan varchar(15))")

def insert_table():
    c.execute("insert into Alyusha_person values('Alyusha','1996-11-12','bhagalpur','BWPP1234')")
    c.execute("insert into Alyusha_person values('Rosalind','1998-10-18','hyderabad','BBGH8451')")
    c.execute("insert into Alyusha_person values('Satwik','2000-12-31','Patna','ABBG1238')")
    c.execute("insert into Alyusha_person values('Zaara','1997-01-05','Mumbai','FGHJ7458')")
    c.execute("insert into Alyusha_person values('Saloni','2001-07-13','Chennai','NNJN4562')")
    con.commit()

def update_table():
    c.execute("UPDATE Alyusha_person SET dob = '1996-12-12' WHERE pan = 'BWPP1234'")
    c.execute("UPDATE Alyusha_person SET address = 'bengaluru' WHERE name = 'Satwik'")
    con.commit()
def del_table():
    c.execute("DELETE FROM Alyusha_person WHERE pan = 'BWPP1234'")
    c.execute("DELETE FROM Alyusha_person WHERE name = 'Satwik'")
    con.commit()
def select_table():
    c.execute('select * from Alyusha_person')
    data=c.fetchall()
    for row in data:
        print(row)

#create_table()
#insert_table()
#update_table()
#del_table()
select_table()
c.close()
con.close()