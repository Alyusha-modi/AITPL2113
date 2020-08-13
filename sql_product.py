import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table product_alyusha(p_id varchar(10),p_name varchar(20),p_des varchar(15),price int)")

def insert_table():
    c.execute("insert into product_alyusha values('hgn789','kurti','A line cotton',670)")
    c.execute("insert into product_alyusha values('hgb856','nivea shower gel','frangipani 400',360)")
    c.execute("insert into product_alyusha values('aaa125','lakme lipstick','red matte 5g',399)")
    c.execute("insert into product_alyusha values('ddt746','dettol handwash','basic 300ml',190)")
    c.execute("insert into product_alyusha values('san456','lifebuoy','sanitizer 50ml',69)")
    con.commit()

def update_table():
    c.execute("UPDATE product_alyusha SET p_desc = 'frangipani400ml' WHERE p_id = 'hgb856'")
    c.execute("UPDATE product_alyusha SET price = 25 WHERE p_name = 'lifebuoy'")
    con.commit()
def del_table():
    c.execute("DELETE FROM product_alyusha WHERE p_id = 'hgb856'")
    con.commit()
def select_table():
    c.execute('select * from product_alyusha')
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