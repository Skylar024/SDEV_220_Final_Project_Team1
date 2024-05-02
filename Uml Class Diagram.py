class ScheduleDB:
    def __init__(self, business_id, business_name, customer_name, set_date):
        self.business_id = business_id
        self.business_name = business_name
        self.customer_name = customer_name
        self.set_date = set_date

class Appointment:
    def __init__(self):
        pass

    def addAppointment(self):
        pass

    def removeAppointment(self):
        pass

    def __repr__(self):
        pass

class Prompts:
    def __init__(self):
        self.empty = "The entry was empty."
        self.divider = "You didn't use a dash to separate month, day, and year."
        self.retry = "Please try again and enter correct date format."
        self.wrong = "Please check your date as you have not entered values for either month, day, year, or your format is wrong."
        self.no_number = "You have not entered number(s) for one or more date segments."
        self.bad_month = "A month value cannot be more than 12."
        self.bad_day = "A day value cannot be more than 31."
        self.bad_date = "The date cannot be in the past."
        self.ask = f"When is the client checking out? (i.e.: {PRESENT.month}-{PRESENT.day + 5}-{PRESENT.year})> "

class Sources:
    def __init__(self):
        pass

    def date_format(self, prompt):
        pass

PRESENT = dt.now()
