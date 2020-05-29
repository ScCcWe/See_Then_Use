"""
install: pip install pymysql, faker
function: 在mysql中添加100条虚拟数据
warning: 这里的数据库 fake_test ，和表 per_info 都是需要你先自建的
file: create_mysql_data.py
author: ScCcWe
time: 2019-12-28
"""
from faker import Faker
import pymysql

fake = Faker("zh-CN")

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='**********',
    charset='utf8',
    db='fake_test')

sql = "insert into per_info(name, idCard, addr, tel) values (%s, %s, %s, %s)"

cursor = conn.cursor()

for i in range(100):
    params = (fake.name(), fake.ssn(), str(fake.city()), fake.phone_number())
    cursor.execute(sql, params)
    conn.commit()

cursor.close()
conn.close()
