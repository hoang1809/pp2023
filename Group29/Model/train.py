import csv 

class Train:
    def __init__(self, id, name, departure, destination, seat, time, ticket_price):
        self.name = name
        self.id = id
        self.departure = departure
        self.destination = destination
        self.seat = seat
        self.time = time
        self.ticket_price = ticket_price

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id 
    def get_departure(self):
        return self.departure
    def get_destination(self):
        return self.destination
    def get_seat(self):
        return self.seat
    def get_time(self):
        return self.time
    def get_ticket_price(self):
        return self.ticket_price

    def set_name(self,name):
        self.name = name
    def set_id(self,id):
        self.id = id
    def set_departure(self,departure):
        self.departure = departure
    def self_destination(self,destination):
        self.destination = destination
    def self_time(self,time):
        self.time = time 
    def self_ticket_price(self,ticket_price):
        self.ticket_price = ticket_price
    
class TrainDatabase:
    train_list = [Train]
    train_list.clear()

    def __init__(self):
        self.trains = []

    def add_Train(self):
        id = input("Enter id of the train: ")
        for x in self.trains:
            if x.id == id:
                print("Train id already exist!")
                return
        train = Train(id,
                      input("Enter name of train: "),
                      input("From: "),
                      input("To: "),
                      int(input("Available seats: ")),
                      input("Departure time: "),
                      float(input("Ticket price: ")))
        
        self.trains.append(train)
        print("Train added!")


    def remove_Train(self):
        train_id = input("Enter train ID: ")
        train = next((x for x in self.trains if x.id == train_id), None)
        if train is None:
            print("Train not found!")
            return
        self.trains.remove(train)
        for x in self.tickets:
            if x.train.id == train_id:
                self.tickets.remove(x)
        print("Train removed!")

    def search_TrainId(self,train):
        train_id = input("Enter train id: ")
        train = next((x for x in self.trains if x.id == train_id),None)
        if train is None:
            print("Train not found")
            return
        for train in self.trains:
            if train.id == train_id:
                print(f"{train.id:<10}{train.name:<15}{train.seat:<10}{train.departure} - {train.destination:<20}{train.time:<10}{train.ticket_price}$")

    def search_TrainDestination(self):
        departure = input("Enter departure: ")
        destination = input("Enter destination: ")
        train = [x for x in self.trains if x.departure == departure and x.destination == destination]
        if not train:
            print("Train not found")
            return
        for x in train:
            print(f"{x.id:<10}{x.name:<15}{x.seat:<10}{x.departure} - {x.destination:<20}{x.time:<10}{x.ticket_price}$")

    def list_Train(self):
        for train in self.trains:
            print(f"{train.id:<10}{train.name:<15}{train.seat:<10}{train.departure} - {train.destination:<20}{train.time:<10}{train.ticket_price}$")


    def list_Passenger(self):
        train_id = input("Enter train id: ")
        train = next((x for x in self.trains if x.id == train_id),None)
        if train is None:
            print("Train not found")
            return
        for ticket in self.tickets:
            if ticket.train.id == train_id:
                print(f"{ticket.passenger_name:<20}{ticket.age:<20}{ticket.phone_number:<20}{ticket.seat_number:<20}{ticket.id}")

    def add_Save(self,train):
        self.train_list.append(train)
        self.save_to_csv(train)

    def save_to_csv(self):
        with open("train.csv", mode='w', newline='') as csv_file:
            fieldnames = ['id', 'name', 'departure', 'destination', 'seat' , 'time', 'ticket_price']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for train in self.train_list:
                writer.writerow({'id': train.get_id(), 
                                 'name': train.get_name(), 
                                 'departure' : train.get_departure(),
                                 'destination' : train.get_destination(), 
                                 'seat' : train.get_seat(), 
                                 'time' : train.get_time(), 
                                 'ticket_price': train.get_ticket_price()})

    def load_csv(self):
        try:
            with open("train.csv", mode = 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for column in csv_reader:
                        id = column['id']
                        name = column['name']
                        departure = column['departure']
                        destination = column['destination']
                        seat = column['seat']
                        time = int(column['time'])
                        ticket_price = int(column['ticket_price'])
                        train = Train(id, name, departure, destination, seat, time, ticket_price)
                        self.add_Train(train)      
        except FileNotFoundError:
            with open("train.csv", mode='w', newline='') as csv_file:
                fieldnames = ['id', 'name', 'departure', 'destination', 'seat' , 'time', 'ticket_price']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

    def print_train_csv(self):
        with open ('train.csv', mode = 'r') as csv_file:
            reader = csv.reader(csv_file)
            for column in reader:
                print(column)

    def idDub(self,id):
        for train in self.train_list:
            if train.get_id() == id:
                return True
        return False


