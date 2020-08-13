import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table cars_alyusha(model varchar(10),manufacturer varchar(20),name varchar(15),price int)")

def insert_table():
    c.execute("insert into cars_alyusha values('hyu155125','hyundai','venue',670000)")
    c.execute("insert into cars_alyusha values('hyu2556','hyundai','creta',999000)")
    c.execute("insert into cars_alyusha values('hyu2589','hyundai','verna',931000)")
    c.execute("insert into cars_alyusha values('hyu2552','hyundai','Aura',581000)")
    c.execute("insert into cars_alyusha values('hyu2578','hyundai','tucson',2230000)")
    con.commit()

def update_table():
    c.execute("UPDATE cars_alyusha SET model = 'hyu7452' WHERE model = 'hyu2589'")
    c.execute("UPDATE cars_alyusha SET price = 932000 WHERE model = 'hyu2589'")
    con.commit()
def del_table():
    c.execute("DELETE FROM cars_alyusha WHERE model = 'hyu2589'")
    con.commit()
def select_table():
    c.execute('select * from cars_alyusha')
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