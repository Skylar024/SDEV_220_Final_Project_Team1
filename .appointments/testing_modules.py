"""
Program: testing_modules.py
Author: Tom Simic
Last date modified: 2024-05-06
Used for testing needs.
"""
# pseudo code:
# connect to iShop.db
# import sqlite3

# conn = sqlite3.connect('iShop.db')
# curs = conn.cursor()
# curs.execute("SELECT *, oid FROM ScheduleDB")
# records = curs.fetchall()
# print(records)
# conn.close()
# The above worked and returned list of tuples
# Test importing appointments module:
# import appointment as A

# schedueld_date = A.ScheduleIt(3, "We In the Woods","Tom")
# print(schedueld_date)
# Above worked but I'm little confused so I emailed the professor

# connect to DBManager module and test db connection
import DBManager as dbm

dbm.DataBaseClass.print_database()