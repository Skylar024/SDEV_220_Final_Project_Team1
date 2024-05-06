"""
Program: appointment.py
Author: Tomi Simic
Last date modified: 2024-04-21
This program is to be used as a module for the final project application for
team project assignment.

NOTE:I changed it a bit so you guys can easier extrapolate what arguments
need to be added. Once we are ready to implement this, we can remove all
the variables starting with 'business_' since those will be suplimented
by the GUI module through business selection. I'll refactor it a bit more
once we have general GUI interaction sorted out.
"""


from dataclasses import dataclass, field


@dataclass
class ScheduleIt:
    """Stores selected business details with the appointment date"""
    from sources import scheduleIt
    business_id: int
    business_name: str
    customer_name: str

    set_date: str = field(default_factory=scheduleIt.addAppointment)


if __name__ == "__main__":
    # business_id = input("Enter Business ID: ")  # check note below
    # business_name = input("Enter Business name: ")  # check note below
    # business_id = input("Enter Customer's full name: ")  # check note below
    # app_date = ScheduleIt(business_id, business_name, business_id)
    # app_date_output = app_date.__dict__
    # # we'll change it to return add_date_output to get the dictionary back
    # print(app_date_output)
    import sys
    arg1, arg2, arg3 = sys.argv[1:]
    ScheduleIt(arg1, arg2, arg3)
    
