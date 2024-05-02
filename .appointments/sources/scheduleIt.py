"""
Program: scheduleIt.py
Author: Tomi Simic
Last date modified: 2024-02-20
This program is to be used as a module for the final project application for
team project assignment.
"""
# pseudo code:

# create class that stores the dates


def addAppointment():
    """Verifies the date entered by the user."""
    from sources import prompts
    user_input = "entry"
    while user_input == 'entry':
        user_input = prompts.date_format(input(prompts.Prompts.ask))
        if isinstance(user_input, str):
            print(user_input)
            print('\n')
            user_input = "entry"
        else:
            return f"{user_input[0]}-{user_input[1]}-{user_input[2]}"


if __name__ == "__main__":
    addAppointment()
