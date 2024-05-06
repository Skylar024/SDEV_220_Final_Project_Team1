"""
Program: DBManager.py
Author: Skylar Thompson
This program is the Database control module
"""
import sqlite3
# import csv
import appointment as A

conn = sqlite3.connect('iShop.db')
curs = conn.cursor()

class DataBaseClass:
    """Controls the insertion and selecting of database entries"""
    business_id: int
    business_name: str
    customer_name: str
    set_date: str

    def submit(self):
        """This Controls the entry of the data into the Database
        Intended to be used by getting all the information from the GUI fields from
        the users input in the GUI using the business_id.get(), business_name.get(),
        customer_name.get(), and set_date.get(). Then inserting that entry into the
        Database, no return needed (unless wanted for a conformation message to
        the user for a successful submission)"""
        curs.execute("INSERT INTO scheduleDB VALUES (:business_id, :business_name, :customer_name, :set_date)",
             {
                 'business_id': business_id.get(),
                 'business_name': business_name.get(),
                 'customer_name': customer_name.get(),
                 'set_date': set_date.get()
             })
        conn.commit()

    def delete_appt(self):
        """This controls deleting entries from the Database
        Intended to be used by getting the business_id from the users input from
        the GUI using the business_id.get() from a 'delete appointment' button (or
        something like it) when it is clicked, no return needed (unless wanted for
        a conformation message to the user for a successful deletion)"""
        b_id = business_id.get()
        sql = f"DELETE FROM scheduleDB WHERE business_id = '{b_id}'"
        curs.execute(sql)
        conn.commit()

    def check_appt(self):
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
    records_list = ''
    for x in temp:
        records_list += x
    return records_list
#-----------------------------------------------------------------------------------------------
#-----------Older methods/functions, not used anymore but kept just in case---------------------
#-----------------------------------------------------------------------------------------------
    # def delAppt(date):
    #     """Old method/function to delete entry form database, requires a date to be passed in"""
    #     month = date[0]
    #     day = date[1]
    #     year = date[2]
    #     date2 = r"'{}-{}-{}'".format(year, month, day)

    #     sql = "DELETE FROM scheduleDB WHERE set_date = {}".format(date2)
    #     curs.execute(sql)
    #     conn.commit()

    # def addAppt(appt):
    #     """Old method/function to insert entry into database, requires full entry dictionary to be passed in"""
    #     BI = appt['business_id']
    #     BN = appt['business_name']
    #     CN = appt['customer_name']
    #     SD = appt['set_date']

    #     curs.execute("INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?, ?, ?, ?)", (BI, BN, CN, SD))
    #     conn.commit()
        
    # def checkApptDate(date):
    #     """Old method/function to check avalibility of appointment date, requires a date to be passed in"""
    #     month = date[0]
    #     day = date[1]
    #     year = date[2]
    #     date2 = r"'{}-{}-{}'".format(year, month, day)
    #     sql = "SELECT * FROM scheduleDB WHERE set_date = {}".format(date2)
    #     curs.execute(sql)
    #     tempR = curs.fetchall()
    #     print("\nAll appointments on: {}".format(date))
        print(tempR)


#Method below are just for spot testing different things
# def printDB():
#     curs.execute('SELECT * FROM scheduleDB')
#     temp = curs.fetchall()
#     for x in temp:
#         print(x)
   
# def printIndex(key):
#     print(A.app_date_output[key])

# #Redundant, Extra way to add appointments via csvfile but only temporarilty (Used for testing)
# def importCSV():
#     with open('schedule.csv') as fin:
#         csvin = csv.reader(fin, delimiter=',')
#         list = []
#         for row in csvin:
#             value = (row[0], row[1], row[2], row[3])
#             list.append(value)
            
#     for row in list:
#         ins = 'INSERT INTO scheduleDB (business_id, business_name, customer_name, set_date) VALUES (?,?,?,?)'
#         curs.execute(ins,row)
