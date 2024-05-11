"""
Program: scheduleIt.py
Author: Tomi Simic
Last date modified: 2024-02-20
This program is to be used as a module for the final project application for
team project assignment. It loops the user until correct input is entered for
the user name and the date.
"""
# Import module(s):
from sources import prompts

# create class that verifies the dates
class ScheduleIt:

    def acceptAppointment():
        """Verifies the date entered by the user."""
        user_input = prompts.date_format(input(prompts.Prompts.ask))
        # Evaluating if return is a string:
        while isinstance(user_input, str):
                print('\n')
                print(user_input)
                print('\n')
                user_input = prompts.date_format(input(prompts.Prompts.ask))
        # Returning date in ISO format if the value is a list:
        return f"{user_input[0]}-{user_input[1]}-{user_input[2]}"


    def acceptName():
        """Verifies user name entered."""
        user_input = prompts.name_format(input(prompts.Prompts.user_name))
        # Evaluationg if the return is a Boolean value:
        while isinstance(user_input, bool):
            print('\n')
            print(prompts.Prompts.bad_name)
            print('\n')
            user_input = prompts.name_format(input(prompts.Prompts.user_name))
        # Returning user's name if it's not a Boolean value
        return user_input


if __name__ == "__main__":
    ScheduleIt()
