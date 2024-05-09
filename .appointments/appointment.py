"""
Program: appointment.py
Author: Tomi Simic
Last date modified: 2024-04-21
This program is to be used as a module for the final project application for
team project assignment.
"""
# Importing needed module(s)
from dataclasses import dataclass, field

# Dataclasss used as caching object for local processing
@dataclass
class SetAppointment:
    """Stores selected business details with the appointment date"""
    from sources import scheduleIt
    business_id: int = -1
    business_name: str = "Default Business Name"
    customer_name: str = field(default_factory=scheduleIt.ScheduleIt.acceptName)
    set_date: str = field(default_factory=scheduleIt.ScheduleIt.acceptAppointment)


if __name__ == "__main__":
    SetAppointment()
    
