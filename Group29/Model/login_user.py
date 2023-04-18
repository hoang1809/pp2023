import csv

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password


    def set_username(self, username):
        self.__username = username
    def set_password(self, password):
        self.__password = password


class UserDatabase:
    userList = [User]

    def addAndSave(self,user):
        self.userList.append(user)
        self.save_to_csv(user)

    def remove_user(self, user):
        self.userList.remove(user)
        self.saveall_to_csv()

    def searchUser(self,username):
        for user in self.userList:
            if user.get_username() == username:
                return user
        return None

    # def update_user(self, user, username=None, password=None):
    #     if username:
    #         user.set_username(username)
    #     if password:
    #         user.set_password(password)
    #     self.save_to_csv()

    def save_to_csv(self,user):
        with open("user.csv", mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([user.get_username(), user.get_password(),user.get_question(),user.get_answer()])

    def saveall_to_csv(self):
        with open("user.csv", mode='w', newline='') as f:
            writer = csv.writer(f)
            for user in self.userList:
                writer.writerow([user.get_username(), user.get_password(), user.get_question(), user.get_answer()])

    def load_from_csv(self):
        try:
            with open("user.csv", mode='r') as f:
                reader = csv.reader(f)
                for line in reader:
                    username,password,question,answer = line
                    user = User(username,password,question,answer)
                    self.userList.append(user)
        except FileNotFoundError:
            k = open("Train_info","w")
            k.close()

    # def login(self, username, password):
    #     for user in self.__user_list:
    #         if user.get_username() == username and user.get_password() == password:
    #             print("Login successful!")
    #             return
    #     print("Invalid username or password.")

def deleteUser(username):
    data = UserDatabase()
    remv = data.searchUser(username)
    data.remove_user(remv)

def set_user_info(uN,pW):
    data = UserDatabase()
    user = User(uN,pW)
    data.addAndSave(user)

def initUser():
    load = UserDatabase()
    UserDatabase.userList.clear()
    load.load_from_csv()


##If password is correct return True, else return false
def checkPassword(username,password):
    k = UserDatabase()
    search = k.searchUser(username)
    if search != None and search.get_password() == password:
        return True
    else:
        return False
    
#If username exist return True, else return false
def checkUsername(username):
    t = UserDatabase()
    search = t.searchUser(username)
    if search != None:
        return True
    else:
        return False

