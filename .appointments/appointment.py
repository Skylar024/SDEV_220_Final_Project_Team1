"""
Program: appointment.py
Author: Tomi Simic
Last date modified: 2024-04-21
This program is to be used as a module for the final project application for
team project assignment.
"""
from dataclasses import dataclass

@dataclass
class ScheduleIt:
    """Stores the schedule for the business"""
    business_id: int
    business_name: str
    set_date = str
    customer_name: str

    def addAppointment(self):
        from sources import prompts
        user_input = "entry"
        while isinstance(user_input, str):
            user_input = prompts.date_format(input("Enter valid date:> "))
            if isinstance(user_input, str):
                print('\n')
            self.set_date = user_input
        return self.set_date