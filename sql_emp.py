import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table Alyusha_employee(emp_id varchar(10),emp_name varchar(20),salary int)")

def insert_table():
    c.execute("insert into Alyusha_employee values('AITPL2500','Alyusha',75000)")
    c.execute("insert into Alyusha_employee values('AITPL2556','Harsh',85000)")
    c.execute("insert into Alyusha_employee values('AITPL2589','Rachna',55000)")
    c.execute("insert into Alyusha_employee values('AITPL2552','Elon',65000)")
    c.execute("insert into Alyusha_employee values('AITPL2578','corey',95000)")
    con.commit()

def update_table():
    c.execute("UPDATE Alyusha_employee SET salary = 70000 WHERE emp_id = 'AITPL2589'")
    c.execute("UPDATE Alyusha_employee SET salary = 80000 WHERE emp_id = 'AITPL2552'")
    con.commit()
def del_table():
    c.execute("DELETE FROM Alyusha_employee WHERE emp_id = 'AITPL2589'")
    c.execute("DELETE FROM Alyusha_employee WHERE emp_id = 'AITPL2578'")
    con.commit()
def select_table():
    c.execute('select * from Alyusha_employee')
    data=c.fetchall()
    for row in data:
        print(row)

#create_table()
#insert_table()
#update_table()
del_table()
select_table()
c.close()
con.close()