import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

class SchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Scheduling System")
        self.root.geometry("500x500")

        tk.Label(self.root, text="Welcome to the Appointment Reservation System.\nPlease review the List of Services and press the button to proceed.",
                 font=('Arial', 14), justify=tk.CENTER).pack(pady=(10, 20))

        tk.Label(self.root, text="List of Services", font=('Arial', 16)).pack(pady=(10, 0))

        self.services = {
            1: ("iMac Repairs", "$99"),
            2: ("iPad Repairs", "$79"),
            # Add other services 
        }
        
        services_text = "\n".join([f"{k}: {v[0]} - {v[1]}" for k, v in self.services.items()])
        self.services_label = tk.Label(self.root, text=services_text, justify=tk.LEFT)
        self.services_label.pack(pady=20)
        
        tk.Button(self.root, text="Start Appointment Reservation", command=self.start_reservation_process).pack(pady=20)

    def start_reservation_process(self):
        service_id = simpledialog.askinteger("Select a Service", "Enter number for service:")
        if service_id not in self.services:
            messagebox.showerror("Error", "Invalid service number.")
            return
        self.service_id = service_id  # Save service ID for DB
        self.send_to_database(self.service_id)  # Send service ID to DB

        self.select_business()  # Continue to select business

    def select_business(self):
        self.businesses = {
            1: "iShop",
            2: "PC-Com",
            # Add businesses here
        }
        
        business_msg = "\n".join([f"{k}: {v}" for k, v in self.businesses.items()])
        business_id = simpledialog.askinteger("Select a Business", f"Please enter the number corresponding to the business you want:\n{business_msg}")
        if business_id not in self.businesses:
            messagebox.showerror("Error", "Invalid business number.")
            return
        business = self.businesses[business_id]

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
        messagebox.showinfo("Appointment Scheduled", f"Appointment at {self.selected_business} is scheduled for {self.date_var.get()} under the name {self.name_var.get()}.")
        self.root.destroy()

    def send_to_database(self, service_id):
        # Connect to SQLite DB
        conn = sqlite3.connect('Final_Project_DB.sqlite')
        cursor = conn.cursor()
        
        # Create table 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ServiceRequests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_id INTEGER NOT NULL
            )
        ''')
        
        # Insert the service ID into DB Table
        cursor.execute('INSERT INTO ServiceRequests (service_id) VALUES (?)', (service_id,))
        
        # Commit and Close DB
        conn.commit()
        conn.close()

        print(f"Service ID {service_id} sent to database.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()
