"""
Program: testing.py
Author: Skylar Thompson
This program is to be used for testing and setting up 
aspects of the database
"""
import sqlite3
import DBManager as DBM

#import appointment as A


conn = sqlite3.connect('iShop.db')
curs = conn.cursor()

curs.execute("DELETE FROM scheduleDB")
conn.commit()

#DBM.submit(45, 'Test', 'TestName', '08-24-2024')
# curs.execute("DELETE FROM scheduleDB WHERE business_id = 45")
# conn.commit()
# servicesDict = {}

# temp = DBM.return_services()
# for x in temp:
#     tempID, tempService = x
#     servicesDict[tempID] = tempService
# print("ServicesDict")
# print(servicesDict)

# businesses = {}

# temp2 = DBM.check_business_from_service(1)
# for x in temp2:
#     tempID, tempBusiness = x
#     businesses[tempID] = tempBusiness
# print("Businesses")
# print(businesses)

# curs.execute("SELECT scheduleDB.business_id, scheduleDB.business_name, business_serviceDB.service_id FROM scheduleDB INNER JOIN business_serviceDB ON scheduleDB.business_name=business_serviceDB.business_name")
# temp2 = curs.fetchall()
# print(temp2)



# -------Use in case DataBase gets deleted-------

# curs.execute('''CREATE TABLE scheduleDB
#     (business_id INT,
#     business_name VARCHAR(50),
#     customer_name VARCHAR(50),
#     set_date DATE)''')

# curs.execute("DELETE FROM scheduleDB")
# conn.commit()
# curs.execute('''CREATE TABLE business_service_table
#             (business_name VARCHAR(50),
#             service_id INT,
#             service VARCHAR(50))''')





# curs.execute("INSERT INTO serviceDB (service_id, service) VALUES (?, ?)", (7, 'Malware/Virus Removal'))
# conn.commit()


# curs.execute('INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?, ?, ?, ?)', (17, 'PC-COM', 'Test', '07-14-2024'))
# conn.commit()


