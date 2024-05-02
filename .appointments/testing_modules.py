# from sources import prompts

# user_input = "entry"
# while isinstance(user_input, str):
#     user_input = prompts.date_format(input("Enter valid date:> "))
#     if isinstance(user_input, str):
#         print('\n')
#     print(user_input)
import datetime

appt = input("date")
print(datetime.datetime.strptime(appt, '%m-%d-%Y'))
