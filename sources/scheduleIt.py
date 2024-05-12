"""
Program: scheduleIt.py
Author: Tomi Simic
Last date modified: 2024-02-20
This program is to be used as a module for the final project application for
team project assignment. It loops the user until correct input is entered for
the user name and the date.
"""
# Import module(s):
from tkinter import messagebox
from sources import prompts

# create class that verifies the dates


class ScheduleIt:

    def acceptAppointment(entry):
        """Verifies the date entered by the user."""
        user_input = prompts.date_format(entry)
        # Evaluating if return is a string:
        if isinstance(user_input, str):
            messagebox.showerror("Invalid date entry", user_input)
            return False
        else:
            # Returning date in ISO format if the value is a list:
            return f"{user_input[0]}-{user_input[1]}-{user_input[2]}"

    def acceptName(entry):
        """Verifies user name entered."""
        user_input = prompts.name_format(entry)
        # Evaluationg if the return is a Boolean value:
        if isinstance(user_input, bool):
            messagebox.showerror("Invalid Name entery",
                                 prompts.Prompts.bad_name)
            return False

        else:
            # Returning user's name if it's not a Boolean value
            return user_input


if __name__ == "__main__":
    ScheduleIt()
