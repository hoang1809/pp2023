import tkinter as tk
from tkinter import messagebox
import random
import csv
        
class TrainManagementSystem:
    def __init__(self,root):
        self.window = root
        self.window.geometry("800x600")
        self.window.title("Train Management System")
        self.window.configure(bg="#F5F5F5")
        self.widgets()
    
    def widgets(self):   

        self.label = tk.Label(self.window, text="Train Management System", font=("Time new roman", 24))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)


        # Frame Train 
        self.train_frame = tk.Frame(self.window)
        self.train_frame.grid(row=1, column=0, padx=10, pady=10)

        self.train_label = tk.Label(self.train_frame, text="Train Management", font=("Time new roman", 18))
        self.train_label.grid(row=0, column=0, columnspan=5, pady=10)

        self.train_add_button = tk.Button(self.train_frame, text="Add", font=("Time new roman", 14), width=10, command=self.add_train_window)
        self.train_add_button.grid(row=1, column=0, padx=10, pady=5)

        self.train_search_button = tk.Button(self.train_frame, text="Search", font=("Time new roman", 14), width=10,command=self.search_train_window)
        self.train_search_button.grid(row=1, column=1, padx=10, pady=5)

        self.train_delete_button = tk.Button(self.train_frame, text="Delete", font=("Time new roman", 14), width=10,command=self.delete_train)
        self.train_delete_button.grid(row=1, column=2, padx=10, pady=5)

        # Frame Train Listbox
        self.train_listbox_frame = tk.Frame(self.train_frame, borderwidth=2, relief="groove")
        self.train_listbox_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.train_listbox_label = tk.Label(self.train_listbox_frame, text="Train List", font=("Time new roman", 14))
        self.train_listbox_label.pack(side="top", padx=10, pady=10)

        self.train_listbox = tk.Listbox(self.train_listbox_frame, width=115, height=30)
        self.train_listbox.pack(side="left", padx=10, pady=10)

        self.train_scrollbar = tk.Scrollbar(self.train_listbox_frame, orient="vertical")
        self.train_scrollbar.config(command=self.train_listbox.yview)
        self.train_scrollbar.pack(side="right", fill="y")

        self.train_listbox.config(yscrollcommand=self.train_scrollbar.set)

        # Frame Ticket
        self.ticket_frame = tk.Frame(self.window)
        self.ticket_frame.grid(row=1, column=1, padx=10, pady=10,sticky="nsew")

        self.ticket_label = tk.Label(self.ticket_frame, text="Ticket Management", font=("Time new roman", 18))
        self.ticket_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.ticket_add_button = tk.Button(self.ticket_frame, text="Add", font=("Time new roman", 14), width=10, command=self.add_ticket_window)
        self.ticket_add_button.grid(row=1, column=0, padx=10, pady=5)

        self.ticket_search_button = tk.Button(self.ticket_frame, text="Search", font=("Time new roman", 14), width=10, command=self.search_ticket_window)
        self.ticket_search_button.grid(row=1, column=1, padx=10, pady=5)
        
        self.ticket_delete_button = tk.Button(self.ticket_frame, text="Delete", font=("Time new roman", 14), width=10, command=self.delete_ticket)
        self.ticket_delete_button.grid(row=1, column=2, padx=10, pady=5)

        # Frame Ticket Listbox
        self.ticket_listbox_frame = tk.Frame(self.ticket_frame, borderwidth=2, relief="groove")
        self.ticket_listbox_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.ticket_listbox_label = tk.Label(self.ticket_listbox_frame, text="Ticket List", font=("Time new roman", 14))
        self.ticket_listbox_label.pack(side="top", padx=10, pady=10)

        self.ticket_listbox = tk.Listbox(self.ticket_listbox_frame, width=115, height=30)
        self.ticket_listbox.pack(side="left", padx=10, pady=10)

        self.ticket_scrollbar = tk.Scrollbar(self.ticket_listbox_frame, orient="vertical")
        self.ticket_scrollbar.config(command=self.train_listbox.yview)
        self.ticket_scrollbar.pack(side="right", fill="y")

        self.ticket_listbox.config(yscrollcommand=self.ticket_scrollbar.set)

        
    #Create Add_train window
    def add_train_window(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Add Train")
        label = tk.Label(self.new_window, text="Add Train Information",font=("Time new roman", 24))
        label.pack()
            
        tk.Label(self.new_window, text="Train_ID", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.train_ID_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.train_ID_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="Train_Name", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.train_name_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.train_name_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="departure", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.departure_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.departure_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="destination", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.destination_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.destination_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="seat", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.seat_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.seat_entry.pack(padx=10, pady=0)
        
        tk.Label(self.new_window, text="time", font=("Time new roman", 10),bg="#F5F5F5").pack(padx=10, pady=10)
        self.time_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.time_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="price", font=("Time new roman", 10),bg="#F5F5F5").pack(padx=10, pady=10)
        self.price_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.price_entry.pack(padx=10, pady=0)

        self.add_button = tk.Button(self.new_window, text="Add Train", command=self.add_train)
        self.add_button.pack(padx=10,pady=20,side=tk.LEFT)

        self.add_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        self.add_button.pack(padx=10,pady=20,side=tk.RIGHT)

    #Add Train    
    def add_train(self):
        train_ID = self.train_ID_entry.get()
        train_name = self.train_name_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        seat = self.seat_entry.get()
        time = self.time_entry.get()
        price = self.price_entry.get()
        
        if not train_ID or not train_name or not departure or not destination or not seat or not time or not price:
            tk.messagebox.showerror("Error", "Please fill out the information completely!")
            return

        for train in self.train_listbox.get(0, tk.END):
            if f"ID: {train_ID}" in train:
                tk.messagebox.showerror("Error", "Train ID already exists!")
                return   
        tk.messagebox.showinfo("Info","Train added!")
        
        self.train_listbox.insert(tk.END, f"ID: {train_ID} - name: {train_name} -  departure: {departure} - destination: {destination} - seat: {seat} - time: {time} - price: {price}")  
    
        rows = [[train_ID, train_name, departure, destination, seat, time, price]]
  
        with open('Train_infor.csv', 'a') as f:
            write = csv.writer(f)
            write.writerows(rows)

#LoadCSV    
    def load_csv(self):
        try:
            with open("Train_info.csv", mode = 'r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                        train_ID = row['ID']
                        train_name = row['name']
                        price = row['price']
                        seat = row['seat']
                        departure = row['departure']
                        time = int(row['time'])
                        destination = int(row['destination'])
                        train = [train_ID, train_name, departure, destination, seat, time, price]
                        self.add_train(train)
        except FileNotFoundError:
            with open("Train_info.csv", mode='w', newline='') as f:
                fieldnames = ['ID', 'name', 'departure', 'destination', 'seat' , 'time', 'ticket_price']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()


    #Create Search_train window
    def search_train_window(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Search Train")
        label = tk.Label(self.new_window, text="Search Train Information",font=("Time new roman", 24))
        label.pack()
            
        tk.Label(self.new_window, text="Train_ID", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.train_ID_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.train_ID_entry.pack(padx=10, pady=0)
        
        tk.Label(self.new_window, text="Departure", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.Departure_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.Departure_entry.pack(padx=10, pady=0)
        
        tk.Label(self.new_window, text="Destination", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.Destination_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.Destination_entry.pack(padx=10, pady=0)

        self.add_button = tk.Button(self.new_window, text="Search Train", command=self.search_train)
        self.add_button.pack(padx=10,pady=20,side=tk.LEFT)

        self.add_button = tk.Button(self.new_window, text="Search DE", command=self.search_train_vjp)
        self.add_button.pack(padx=10,pady=20,side=tk.LEFT)

        self.add_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        self.add_button.pack(padx=10,pady=20,side=tk.RIGHT)

    #Search Train
    def search_train(self):
        train_ID = self.train_ID_entry.get()
        for i in range(self.train_listbox.size()):
            if train_ID == self.train_listbox.get(i).split(" ")[1]:
                self.train_listbox.selection_clear(0, tk.END)
                self.train_listbox.selection_set(i)
                self.train_listbox.activate(i)
                

    def search_train_vjp(self):
        dep = self.Departure_entry.get()
        des = self.Destination_entry.get()
        for i in range(self.train_listbox.size()):
            if dep == self.train_listbox.get(i).split(" ")[8] and des == self.train_listbox.get(i).split(" ")[11]:
                self.train_listbox.selection_set(i)
                self.train_listbox.activate(i)
    

    #Delete Train
    def delete_train(self):
        selection = self.train_listbox.curselection()
        if len(selection) > 0:
            train_id = self.train_listbox.get(selection[0]).split(" ")[1]
            self.train_listbox.delete(selection[0])
            i = 0
            while i < self.ticket_listbox.size():
                if train_id in self.ticket_listbox.get(i):
                    self.ticket_listbox.delete(i)
                else:
                    i += 1
    
    #Create Add_ticket window
    def add_ticket_window(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Add Ticket")
        label = tk.Label(self.new_window, text="Add Ticket Information",font=("Time new roman", 24))
        label.pack()
            
        tk.Label(self.new_window, text="Train_ID", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.train_ID_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.train_ID_entry.pack(padx=10, pady=0)


        tk.Label(self.new_window, text="Passenger name", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.passenger_name_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.passenger_name_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="Phone number", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.phone_number_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.phone_number_entry.pack(padx=10, pady=0)

        tk.Label(self.new_window, text="Date of birth", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.dob_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.dob_entry.pack(padx=10, pady=0)

        self.add_button = tk.Button(self.new_window, text="Add Ticket", command=self.add_ticket)
        self.add_button.pack(padx=10,pady=20,side=tk.LEFT)

        self.add_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        self.add_button.pack(padx=10,pady=20,side=tk.RIGHT)
       

    #Add Ticket
    def add_ticket(self):
        train_ID = self.train_ID_entry.get()
        ticket_id =random.randint(10000,99999)
        passenger_name = self.passenger_name_entry.get()
        phone_number = self.phone_number_entry.get()
        dob = self.dob_entry.get()
        if not train_ID or not passenger_name or not phone_number or not dob:
            tk.messagebox.showerror("Error", "Please fill out the information completely!")
            return

        #Check Train Id exists
        train_ID_exists = False
        for train in self.train_listbox.get(0, tk.END):
            if f"ID: {train_ID}" in train:
                train_ID_exists = True
            break
        if not train_ID_exists:
           tk.messagebox.showerror("Error", "Train ID does not exist!")
        return
        
        for ticket in self.ticket_listbox.get(0, tk.END):
            if f"Ticket_ID: {ticket_id}" in ticket:
                tk.messagebox.showerror("Error", "Train ID already exists!")
                return   
        tk.messagebox.showinfo("Info","Ticket added!")
        
        self.ticket_listbox.insert(tk.END, f"Ticket_ID: {ticket_id} - Train_ID: {train_ID} - passenger name: {passenger_name} - Phone: {phone_number} - dob: {dob}")  
    
        rows = [[ticket_id, train_ID, passenger_name, phone_number, dob]]
  
        with open('Ticket_info.csv', 'a') as fs:
            write = csv.writer(fs)
            write.writerows(rows)
        
        #Check available seat
        for i in range(self.train_listbox.size()):
            if f"ID: {train_ID}" in self.train_listbox.get(i):
                train_ID_exists = True
                train_item = self.train_listbox.get(i)
                train_item_parts = train_item.split(" - ")
                for j, part in enumerate(train_item_parts):
                    if part.startswith("seat"):
                        seat = int(part.split(":")[1])
                        if seat == 0:
                            tk.messagebox.showerror("Error", "No available seat!")
                            return
                        new_train_item_parts = train_item_parts.copy()
                        new_train_item_parts[j] = f"seat: {seat - 1}"
                        new_train_item = " - ".join(new_train_item_parts)
                        self.train_listbox.delete(i)
                        self.train_listbox.insert(i, new_train_item)
                break
        
        #Check Ticket Id exist
        #for ticket in self.ticket_listbox.get(0, tk.END):
        #    if f"ticket_id: {ticket_id}" in ticket:
        #       tk.messagebox.showerror("Error", "Ticket ID already exists!")
        #        return
        #self.ticket_listbox.insert(tk.END, f"ID: {train_ID} - ticket_id: {ticket_id} - passenger_name: {passenger_name} - phone_number: {phone_number} - dob: {dob}")

    #Create Search Ticket window:
    def search_ticket_window(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Search Ticket")
        label = tk.Label(self.new_window, text="Search Ticket Information",font=("Time new roman", 24))
        label.pack()
            
        tk.Label(self.new_window, text="Ticket_ID", font=("Time new roman", 10), bg="#F5F5F5").pack(padx=10, pady=10)
        self.ticket_ID_entry = tk.Entry(self.new_window, font=("Time new roman", 10), width=20)
        self.ticket_ID_entry.pack(padx=10, pady=0)

        self.add_button = tk.Button(self.new_window, text="Search Ticket", command=self.search_ticket)
        self.add_button.pack(padx=10,pady=20,side=tk.LEFT)

        self.add_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        self.add_button.pack(padx=10,pady=20,side=tk.RIGHT)

    #Search Ticket
    def search_ticket(self):
        ticket_id = [x for x in self.ticket_listbox.size()]
        for i in range(self.ticket_listbox.size()):
            if ticket_id == self.ticket_listbox.get(i).split(" ")[4]:
                self.ticket_listbox.selection_clear(0, tk.END)
                self.ticket_listbox.selection_set(i)
                self.ticket_listbox.activate(i)
            if not ticket_id:
                print("No ticket with given infomation!")
            return
        print(f"All ticket of :")
        for x in ticket_id:
            print(f"{x.id:<15}{x.train.id:<15}{x.train.departure} - {x.train.destination:<20}{x.time:<10}{x.seat}")

    #Delete Ticket
    def delete_ticket(self):
        selection = self.ticket_listbox.curselection()
        if len(selection) > 0:
            self.ticket_listbox.delete(selection[0])

if __name__=='__main__':
    root = tk.Tk()
    train_management_system = TrainManagementSystem(root)
    root.mainloop()