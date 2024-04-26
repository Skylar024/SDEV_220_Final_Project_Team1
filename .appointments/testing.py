import sqlite3
conn = sqlite3.connect('iShop.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE scheduleDB
    (business_id INT PRIMARY KEY,
    business_name VARCHAR(50),
    customer_name VARCHAR(50),
    set_date DATE)''')