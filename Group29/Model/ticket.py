import csv
import random


class Ticket:
    def __init__(self, train, id, price, seat_number, passenger_name, phone_number, age):
        self.train = train
        self.id = id
        self.price = price
        self.seat_number = seat_number
        self.passenger_name = passenger_name
        self.phone_number = phone_number
        self.age = age

    def get_train(self):
        return self.train
    def get_id(self):
        return self.id
    def get_price(self):
        return self.price
    def get_seat_number(self):
        return self.seat_number
    def get_passenger_name(self):
        return self.passenger_name
    def get_phone_number(self):
        return self.phone_number
    def get_age(self):
        return self.age
    
    def set_train(self,train):
        self.train = train
    def set_id(self,id):
        self.id = id
    def set_price(self,price):
        self.price = price
    def set_seat_number(self,seat_number):
        self.seat_number = seat_number
    def set_passenger_name(self,passenger_name):
        self.passenger_name = passenger_name
    def set_phone_number(self,phone_number):
        set.phone_number = phone_number
    def set_age(self,age):
        set.age = age


class TicketDatabase:
    ticket_list = [Ticket]
    ticket_list.clear()


    def __init__(self):
        self.tickets = []

    def add_Ticket(self):
        train_id = input("Enter train ID: ")
        train = next((x for x in self.trains if x.id == train_id), None)
        if train is None:
            print("Train not found")
            return
        if train.seat == 0:
            print("No available seat")
            return
        price = train.ticket_price
        seat_number = train.seat
        ticket_id = random.randint(10000,99999)
        while next((x for x in self.tickets if x.id == ticket_id), None) is not None:
            ticket_id = random.randint(10000,99999)
        ticket = Ticket(train,
                        ticket_id,
                        price,
                        seat_number,
                        input("Passenger name: "),
                        input("Phone number: "),
                        input("Age: "))
        self.tickets.append(ticket)
        train.seat -= 1
        print("Ticket added!")
        
        


    def remove_Ticket(self):
        ticket_id = int(input("Enter ticket ID: "))
        ticket = next((x for x in self.tickets if x.id == ticket_id), None)
        if ticket is None:
            print("Ticket not found!")
            return
        self.tickets.remove(ticket)
        train = next((x for x in self.trains if x.id == ticket.train.id), None)
        train.seat += 1
        print("Ticket removed!")
        


    def search_Ticket(self):
        name = input("Enter passenger name: ")
        phone = input("Enter passenger phone number: ")
        ticket = [x for x in self.tickets if x.passenger_name == name and x.phone_number == phone]
        if not ticket:
            print("No ticket with given infomation!")
            return
        print(f"All ticket of {name} - {phone}:")
        for x in ticket:
            print(f"{x.id:<15}{x.train.id:<15}{x.train.departure} - {x.train.destination:<20}{x.train.time:<10}{x.seat_number}")
        

    def add_Save(self,ticket):
        self.ticket_list.append(ticket)
        self.save_to_csv(ticket)

    def save_to_csv(self):
        with open("ticket.csv", mode='w', newline='') as csv_file: 
            fieldnames = ['train', 'id', 'price', 'seat_number', 'passenger_name', 'phone_number', 'age']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for ticket in self.ticket_list:
                writer.writerow({'train': ticket.get_train(), 
                                 'id': ticket.get_train(), 
                                 'price': ticket.get_price(), 
                                 'seat_number':ticket.get_seat_number(), 
                                 'passenger_name': ticket.get_passenger_name(), 
                                 'phone_number': ticket.get_phone_number(), 
                                 'age': ticket.get_age()})


    def load_csv(self):
        try:
            with open("ticket.csv", mode = 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                        train = row['train']
                        id = row['id']
                        price = row['price']
                        seat_number = row['seat_number']
                        passenger_name = row['passenger_name']
                        phone_number= int(row['phone_number'])
                        age = int(row['age'])
                        ticket = Ticket(train, id, price, seat_number, passenger_name, phone_number, age)
                        self.add_Ticket(ticket)
        except FileNotFoundError:
            with open("ticket.csv", mode='w', newline='') as csv_file:
                fieldnames = ['id', 'name', 'departure', 'destination', 'seat' , 'time', 'ticket_price']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

    def print_ticket_csv(self):
        with open ('ticket.csv', mode = 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)


    def idDub(self,id):
        for ticket in self.ticket_list:
            if ticket.get_id() == id:
                return True
        return False
    



