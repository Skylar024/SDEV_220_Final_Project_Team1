"""
Program: testing.py
Author: Skylar Thompson
This program is to be used for testing and setting up aspects of the database
"""
import sqlite3
import DBManager as DBM
#import appointment as A


conn = sqlite3.connect('iShop.db')
curs = conn.cursor()

# -------Use in case DataBase gets deleted-------

# curs.execute('''CREATE TABLE scheduleDB
#     (business_id INT PRIMARY KEY,
#     business_name VARCHAR(50),
#     customer_name VARCHAR(50),
#     set_date DATE)''')

# curs.execute("UPDATE scheduleDB SET set_date = '06-26-2024' WHERE business_id = '5'")
# conn.commit()

# curs.execute('INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?, ?, ?, ?)', (17, 'PC-COM', 'Test', '07-14-2024'))
# conn.commit()

# curs.execute("DELETE FROM scheduleDB WHERE business_id = '17'")
# conn.commit()

#DBM.printDB()
BNAME = "iShop"
record_list = f"Appointments for: {BNAME}\n"
sql = f"SELECT * FROM scheduleDB WHERE business_name = '{BNAME}'"
curs.execute(sql)
records = curs.fetchall()
for x in records:
    record_list += "Business ID: " + str(x[0]) + "\t\t" + "Business Name: " + str(x[1]) + "\t\t" + "Customer Name: " + str(x[2]) + "\t\t" + "Appointment Date: " + str(x[3]) + "\n"
print(record_list)
