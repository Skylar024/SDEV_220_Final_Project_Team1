"""
Program: appointment.py
Author: Tomi Simic
Last date modified: 2024-04-21
This program is to be used as a module for the final project application for
team project assignment.
"""
from dataclasses import dataclass, field

@dataclass
class ScheduleIt:
    """Stores the schedule for the business"""
    business_id: int
    business_name: str
    customer_name: str

    def addAppointment():
        from sources import prompts
        user_input = "entry"
        while isinstance(user_input, str):
            user_input = prompts.date_format(input("Enter valid date:> "))
            if isinstance(user_input, str):
                print(user_input)
                print('\n')
            # ScheduleIt.set_date = date
            return f"{user_input[0]}-{user_input[1]}-{user_input[2]}"

        # return self.user_input
    
    set_date: str = field(default_factory = addAppointment)

# unsure which format is needed for the other module.
# iso_date = f"{app_date[0]}-{app_date[1]}-{app_date[2]}"
# display_date = f"{app_date[1]}-{app_date[2]}-{app_date[0]}"
#testing needs
# print(app_date, iso_date, display_date)
app_date = ScheduleIt(1, "We in the Woods", 'Tom Simic')
app_date_output = app_date.__dict__
print(app_date_output)
