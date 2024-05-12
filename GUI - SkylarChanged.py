"""
Program: GUI - SkylarChanged.py -> to be renamed in final iteration
Authors: Nathan Santiago Sepe, Skylar Thompson, Tomi Simic
Last date modified: 2024-05-11
This program is to be used for the group project assigment for SDEV220.
"""
# pseudo code:
# Import needed modules
# Create the main Tkinter window class with nested functions


import tkinter as tk
from tkinter import simpledialog, messagebox
import DBManager as DBM
from sources import scheduleIt


class SchedulingApp:
    """Provides the main UI to the user."""

    def __init__(self, root):
        """Defining default attributes for the UI."""
        # Main window:
        self.root = root
        self.root.title("Appointment Scheduling System")
        self.root.geometry("600x350+200+80")
        # self.root.attributes("-alpha", 0.95)
        self.root.configure(background='#963505')
        # self.root.attributes("-fullscreen", 1)
        # enable the close icon
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)

        tk.Label(self.root, text="Welcome to the Appointment Reservation System.\nPlease review the List of Services and press the button to proceed.", foreground="#d36d13", background='#963505',
                 font=('Arial', 14), justify=tk.CENTER).pack(pady=(10, 20))

        tk.Label(self.root, text="List of Services", background='#458466', foreground="#963505",
                 font=('Arial', 16)).pack(pady=(10, 0))
        # Connecting to database and pulling service information:
        self.services = {}
        servicesList = DBM.return_services()
        for x in servicesList:
            tempID, tempService = x
            self.services[tempID] = tempService
        # Displaying information to the user:
        services_text = "\n".join(
            [f"{k}: {v}" for k, v in self.services.items()])
        self.services_label = tk.Label(
            self.root, text=services_text, justify=tk.LEFT, background='#963505', foreground="#458466",)
        self.services_label.pack(pady=20)

        # Appointment reservation button
        tk.Button(self.root, text="Start Appointment Reservation", background='#458466',
                  command=self.start_reservation_process).pack(pady=20)

    def start_reservation_process(self):

        service_id = simpledialog.askinteger(
            "Select a Service", "Enter number for service:")
        if service_id not in self.services:
            messagebox.showerror("Error", "Invalid service number.")
            return
        service = self.services[service_id]
        # -------------------------------------------------#
        self.businesses = {}
        businessList = DBM.check_business_from_service(service)
        for x in businessList:
            tempID, tempBusiness = x
            self.businesses[tempID] = tempBusiness

        # -------------------------------------------------#
        business_msg = "\n".join(
            [f"{k}: {v}" for k, v in self.businesses.items()])
        business_id = simpledialog.askinteger(
            "Select a Business", f"Please enter the number corresponding to the business you want for {service}:\n{business_msg}")
        if business_id not in self.businesses:
            messagebox.showerror("Error", "Invalid business number.")
            return
        business = self.businesses[business_id]

        self.selected_service = service
        self.selected_business = business

        self.enter_customer_details()

    def enter_customer_details(self):
        """Capture customer name and the desired date of the appointment."""
        # Setting default window variables
        self.details_window = tk.Toplevel()
        self.details_window.grab_set()
        self.details_window.title("Customer Details")
        self.details_window.geometry("400x300")
        self.name_text = "Please enter your full name (i.e: John Smith)"
        self.date_text = "Enter date (MM-DD-YYYY):"
        # Setting name label and input field
        self.cust_name_label = tk.Label(
            self.details_window, text=self.name_text)
        self.cust_name_label.pack(pady=10)
        self.cust_name_field = tk.Entry(
            self.details_window, textvariable=self.name_text)
        self.cust_name_field.pack()
        # Setting date label and input field
        self.date_label = tk.Label(
            self.details_window, text=self.date_text)
        self.date_label.pack(pady=10)
        self.date_field = tk.Entry(
            self.details_window, textvariable=self.date_text)
        self.date_field.pack()
        # Setting up Submit button
        self.submit_button = tk.Button(
            self.details_window, text="Submit", command=self.input_verification)
        self.submit_button.pack(pady=20)

    def input_verification(self):
        """Providing interaction with the user during name and date verification."""
        user_name = scheduleIt.ScheduleIt.acceptName(
            self.cust_name_field.get())
        appt_date = scheduleIt.ScheduleIt.acceptAppointment(
            self.date_field.get())
        if not appt_date:
            self.date_field.delete(0, tk.END)
            self.date_field.focus_set()
        elif not user_name:
            self.cust_name_field.delete(0, tk.END)
            self.cust_name_field.focus_set()
        else:
            self.schedule_appointment()

    def schedule_appointment(self):
        # ---------------------------------------------------------------#
        DBM.submit(self.selected_business,
                   self.cust_name_field, self.date_field)
        # ---------------------------------------------------------------#
        messagebox.showinfo("Appointment Scheduled", f"Appointment for {self.selected_service} at {
                            self.selected_business} is scheduled for {self.date_field.get()} under the name {self.cust_name_field.get()}.")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()
