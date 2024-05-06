# Nathan Sepe, Tomislav Simic, Skylar Thompson, and William Troutman
# Appointment Schedular
# 05/02/2024
# SDEV-220 Final Project

import tkinter as tk
from tkinter import simpledialog, messagebox
import DBManager
import appointment
from sources import prompts

class SchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Scheduling System")
        self.root.geometry("600x600")
        
        
        tk.Button(self.root, text="Reserve an Appointment", command=self.open_service_window).pack(pady=20)
    
    def open_service_window(self):
        self.service_window = tk.Toplevel(self.root)
        self.service_window.title("Select a Service")
        
        # Services and their prices
        services = {
            "iMac Repairs": "~$750-$1000",
            "iPad Pro Repairs": "~$200-$400",
            "iPad Repairs": "$80-$250",
            "MacBook Pro Repairs": "~$600-$1000",
            "MacBook Air Repairs": "~$400-$600",
            "Data Recovery/Migration": "$50-$100",
            "Screen Replacements": "~$250-$500",
            "Malware/Virus Removal": "$70",
            "Motherboard Replacement": "~$200-$400",
            "Dusting/Cleaning": "$50"
        }
        
        for service, price in services.items():
            button = tk.Button(self.service_window, text=f"{service} - {price}", 
                               command=lambda s=service, p=price: self.schedule_appointment(s, p))
            button.pack(pady=10)
    
    def schedule_appointment(self, service, price):
        self.service_window.destroy()
        date_input = simpledialog.askstring("Appointment Date", "Enter the date for your appointment (YYYY-MM-DD):")
        
        #Use prompts.py to validate
        validation_response = prompts.date_format(date_input)
        if "retry" in validation_response:
            messagebox.showerror("Date Error", validation_response)
            return  # Stops the appointment scheduling process if the date is invalid
        
        # Use the appointment.py to validate 
        schedule_instance = appointment.ScheduleIt(1, service, "Customer Name")
        schedule_instance.set_date = date_input
        
        DBManager.addAppt(schedule_instance.__dict__)
        
        messagebox.showinfo("Appointment Scheduled", f"Your appointment for {service} on {date_input} has been scheduled.")
    

# Setup database
# DBManager.setupDB()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    app.root.mainloop()

