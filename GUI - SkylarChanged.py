import tkinter as tk
from tkinter import simpledialog, messagebox
import DBManager as DBM
from sources import scheduleIt

class SchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Scheduling System")
        self.root.geometry("600x600")

        tk.Label(self.root, text="Welcome to the Appointment Reservation System.\nPlease review the List of Services and press the button to proceed.",
                 font=('Arial', 14), justify=tk.CENTER).pack(pady=(10, 20))

        tk.Label(self.root, text="List of Services", font=('Arial', 16)).pack(pady=(10, 0))
        #--------------------------------------------------#
        self.services = {}
        servicesList = DBM.return_services()
        for x in servicesList:
            tempID, tempService = x
            self.services[tempID] = tempService
        #--------------------------------------------------#    
        services_text = "\n".join([f"{k}: {v}" for k, v in self.services.items()])
        self.services_label = tk.Label(self.root, text=services_text, justify=tk.LEFT)
        self.services_label.pack(pady=20)
        
        tk.Button(self.root, text="Start Appointment Reservation", command=self.start_reservation_process).pack(pady=20)

    def start_reservation_process(self):
        
        
        service_id = simpledialog.askinteger("Select a Service", "Enter number for service:")
        if service_id not in self.services:
            messagebox.showerror("Error", "Invalid service number.")
            return
        service = self.services[service_id]
        #-------------------------------------------------#
        self.businesses = {}
        businessList = DBM.check_business_from_service(service)
        for x in businessList:
            tempID, tempBusiness = x
            self.businesses[tempID] = tempBusiness
            
        #-------------------------------------------------#
        business_msg = "\n".join([f"{k}: {v}" for k, v in self.businesses.items()])
        business_id = simpledialog.askinteger("Select a Business", f"Please enter the number corresponding to the business you want for {service}:\n{business_msg}")
        if business_id not in self.businesses:
            messagebox.showerror("Error", "Invalid business number.")
            return
        business = self.businesses[business_id]

        self.selected_service = service
        self.selected_business = business

        self.enter_customer_details()

    def enter_customer_details(self):
        self.details_window = tk.Toplevel(self.root)
        self.details_window.title("Customer Details")
        self.details_window.geometry("400x300")

        tk.Label(self.details_window, text="Enter your name:").pack(pady=10)
        self.name_var = tk.StringVar()
        tk.Entry(self.details_window, textvariable=self.name_var).pack()
        
        tk.Label(self.details_window, text="Enter date (MM-DD-YYYY):").pack(pady=10)
        self.date_var = tk.StringVar()
        tk.Entry(self.details_window, textvariable=self.date_var).pack()
        
        tk.Button(self.details_window, text="Submit", command=self.schedule_appointment).pack(pady=20)

    def schedule_appointment(self):
        #---------------------------------------------------------------#
        DBM.submit(self.selected_business, self.name_var, self.date_var)
        #---------------------------------------------------------------#
        messagebox.showinfo("Appointment Scheduled", f"Appointment for {self.selected_service} at {self.selected_business} is scheduled for {self.date_var.get()} under the name {self.name_var.get()}.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()
