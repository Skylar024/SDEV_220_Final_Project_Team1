"""
Program: scheduleIt.py
Author: Tomi Simic
Last date modified: 2024-02-20
This program is to be used as a module for the final project application for
team project assignment.
"""
# pseudo code:
# import needed modules
# create class that stores prompts
# create class that stores the dates

# Importing needed module(s):
from dataclasses import dataclass
from datetime import datetime as dd
import calendar as ca






@dataclass
class ScheduleIt:
    """Stores the schedule for the business"""
    business_id: int
    business_name: str
    set_date = str
    customer_name: str
    # services: str

    def addAppointment(self):
        pass

    def removeAppointment(self):
        pass

    def __repr__(self):
        return f"{self.business_name}, {self.set_date} current date\
and time: {ca.da}"


if __name__ == "__main__":
    appointment = ScheduleIt(1, "WeInTheWoods", "today")
    print(appointment)
