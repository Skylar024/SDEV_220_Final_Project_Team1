"""
Program: DBManager.py
Author: Skylar Thompson
This program is the Database control module
"""
import sqlite3
#import csv
import appointment as A

conn = sqlite3.connect('iShop.db')
curs = conn.cursor()

def submit(business_name, customer_name, set_date):
    """This Controls the entry of the data into the Database
    Intended to be used by getting all the information from the GUI fields from
    the users input in the GUI using the business_id.get(), business_name.get(),
    customer_name.get(), and set_date.get(). Then inserting that entry into the
    Database, no return needed (unless wanted for a conformation message to
    the user for a successful submission)"""
    business_id = get_business_id(business_name)
    
    
    # sql = f"INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES ({business_id}, '{business_name}', '{customer_name}', '{set_date}')"
    # curs.execute(sql)
    # conn.commit()
    
    curs.execute("INSERT INTO scheduleDB VALUES (:business_id, :business_name, :customer_name, :set_date)",
        {
            'business_id': business_id,
            'business_name': business_name,
            'customer_name': customer_name.get(),
            'set_date': set_date.get()
        })
    conn.commit()

def get_business_id(BN):
    sql = f"SELECT DISTINCT business_id FROM business_service_table WHERE business_name = '{BN}'"
    curs.execute(sql)
    temp = curs.fetchone()
    temp2 = temp[0]
    return(temp2)
    
def delete_appt():
    """This controls deleting entries from the Database
    Intended to be used by getting the business_id from the users input from
    the GUI using the business_id.get() from a 'delete appointment' button (or
    something like it) when it is clicked, no return needed (unless wanted for
    a conformation message to the user for a successful deletion)"""
    b_id = business_id.get()
    sql = f"DELETE FROM scheduleDB WHERE business_id = '{b_id}'"
    curs.execute(sql)
    conn.commit()

def check_appt():
    """This controls checking entries in the Database
    Intended to be used by getting the date from the users input from the GUI
    using the set_date.get() from a 'check date available' button (or something like it).
    Then selecting every entry with that date then returning all those entries."""
    record_list = f"Appointments for: {business_name.get()}\n"
    b_name = business_name.get()
    sql = f"SELECT * FROM scheduleDB WHERE business_name = '{b_name}'"
    curs.execute(sql)
    records = curs.fetchall()
    for x in records:
        record_list += "Business ID: " + str(x[0]) + "\t\t" + "Business Name: " + str(x[1]) + "\t\t" + "Customer Name: " + str(x[2]) + "\t\t" + "Appointment Date: " + str(x[3]) + "\n"
    return record_list

def print_database():
    """This controls printing the entire Database
    Intended to be used by returning the entire Database when a 'print all
    appointments' button (or something like it) is clicked in the GUI"""
    curs.execute("SELECT * FROM scheduleDB")
    temp = curs.fetchall()
    # records_list = []
    for x in temp:
        # records_list += x
        print(x)
        
def print_serviceDB():
    """This controlls printing the entire serviceDB"""
    curs.execute("SELECT * FROM serviceDB")
    temp = curs.fetchall()
    for x in temp:
        print(x)

def check_business_from_service(service):
    
    sql = f"SELECT business_id, business_name FROM business_service_table WHERE service = '{service}'"
    curs.execute(sql)
    temp = curs.fetchall()
    return temp

def return_services():
    curs.execute("SELECT DISTINCT service_id, service FROM business_service_table")
    temp = curs.fetchall()
    return temp