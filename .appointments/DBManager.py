import sqlite3
import csv
import sqlalchemy as SA
import appointment as A

conn = sqlite3.connect('iShop.db')
curs = conn.cursor()

def delAppt():
    curs.execute("DELETE FROM scheduleDB")
    conn.commit()
    
def addAppt(appt):
    BI = appt['business_id']
    BN = appt['business_name']
    CN = appt['customer_name']
    SD = appt['set_date']
    
    curs.execute("INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?, ?, ?, ?)", (BI, BN, CN, SD))
    conn.commit()
    

#This is just used to print what is currently in the database
def printDB():
    #conn = SA.create_engine('sqlite://')
    curs.execute('SELECT * FROM scheduleDB')
    temp = curs.fetchall()
    print(temp)

 
#Method below are just for spot testing different things  
def testCSV():
    with open('schedule.csv') as fin:
        csvin = csv.reader(fin, delimiter=',')
        list = []
        for row in csvin:
            value = (row[0], row[1], row[2], row[3], row[4])
            list.append(value)
    print(list)
    
def printIndex(key):
    print(A.app_date_output[key])

def checkApptDate(date):
    apptList = []
    with open('schedule.csv') as fin:
        csvin = csv.reader(fin, delimiter=',')
        list = []
        for row in csvin:
            value = (row[0], row[1], row[2], row[3])
            list.append(value)
    for x in list:
        if (x[3] == date):
            apptList.append(x)
    print("All appointments on {}:".format(date))
    if(apptList != []):
        print(apptList)
    else:
        print("None")

def checkApptDate2(date):
    curs.execute('SELECT * FROM scheduleDB WHERE set_date = {}'.format(date))

#Redundant, Extra way to add appointments via csvfile but only temporarilty (Used for testing)
def importCSV():
    with open('schedule.csv') as fin:
        csvin = csv.reader(fin, delimiter=',')
        list = []
        for row in csvin:
            value = (row[0], row[1], row[2], row[3])
            list.append(value)
            
    for row in list:
        ins = 'INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?,?,?,?)'
        curs.execute(ins,row)
        
        
#curs.execute("INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (%d,%s,%s,%s)" % (BI, BN, CN, SD))