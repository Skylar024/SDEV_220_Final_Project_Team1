from datetime import datetime as dt
from dataclasses import dataclass

# setting constant:
PRESENT = dt.now()

# Creating dataclasses:


@dataclass
class Prompts:
    """Prompt jumpbox"""
    empty: str = "The entry was empty."
    divider: str = "You didn't use a dash to separate month, day, and year."
    retry: str = "Please try again and enter correct date format."
    wrong: str = "Please check your date as you have not entered values for either month, day, year, or your format is wrong."
    no_number: str = "You have not entered number(s) for one or more date segments."
    bad_month: str = "A month value cannot be more than 12."
    bad_day: str = "A day value cannot be more than 31."
    bad_date: str = "The date cannot be in the past."
    bad_day_count: str = "Selected month doesn't have that many days."
    ask: str = f"When would you like to schedule the appointment? (i.e.: ({PRESENT.month}\
-{PRESENT.day + 5}-{PRESENT.year}) > "


def date_format(prompt):
    """Verifying user input for correct date entry"""
    # Collecting date entries into single unit:
    schedule = []
    # Check for empty entry:
    if prompt == "":
        return f"{Prompts.empty} {Prompts.retry}"
    # Checking for correct separator:
    elif '-' not in prompt:
        return f"{Prompts.divider} {Prompts.retry}"
    else:
        # Checking for correct count of values entered:
        if len(prompt.split('-')) < 3:
            return f"{Prompts.wrong} {Prompts.retry}"
        else:
            # Separating user's input into year, month, and day:
            month, day, year = prompt.split('-')
            # Verifying the user is using only numbers in date entry:
            if month.isnumeric() is False or day.isnumeric() is False \
                    or year.isnumeric() is False:
                return f"{Prompts.no_number} {Prompts.retry}"
            # Verifying the upper limit for month and day
            elif int(month) > 12:
                return f"{Prompts.bad_month} {Prompts.retry}"
            elif int(day) > 31:
                return f"{Prompts.bad_day} {Prompts.retry}"
            # Verifying the date wasn't entered in the past
            elif int(year) < PRESENT.year or int(month) < PRESENT.month or int(day) < PRESENT.day:
                return f"{Prompts.bad_date} {Prompts.retry}"
            try:
                dt.strptime(f"{year}-{month}-{day}", '%Y-%m-%d')
            except ValueError:
                return f"{Prompts.bad_day_count} {Prompts.retry}"
            else:
                # Populating the list holding individual values:
                schedule.append(year)
                schedule.append(month)
                schedule.append(day)
        return schedule


if __name__ == "__main__":
    Prompts()
