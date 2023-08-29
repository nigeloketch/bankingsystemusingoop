#parent Class :user
#holds details about a user(9 to 13)
#Has a function to show user details(15 to 17)
#Child class : Bank(21 to 24)
#stores details about the account balance
#stores details about the amount
#allows for deposits(25 to 28),withdrawal30 to 35,view balnce

#parent
class User ():
    def __init__(self,name,age,gender):
      self.name = name
      self.age= age  
      self.gender= gender

    def show_details(self):
       print("")
       print("Name: ",self.name,"Age:",self.age ,"Gender",self.gender )

#child class
class Bank(User):
   def __init__(self, name, age, gender):
      super().__init__(name, age, gender)
      self.balance = 0
def deposit (self,amount):
   self.amount = amount
   self.balance = self.balance + self.amount
   print("Account balance has been updated :$",self.balance)

def withdrawal(self,amount):
   self.amount = amount
   if (self.amount > self.balance):
      print ("Insufficient Balance.Balance Available : $",self.balance)
   else:self.balance = self.balance - self.amount
print("Account balance has been updated:$",self.balance)

def view__balance(self):
   self.show_details()
   print("Account balance has been updated:$",self.balance)



 
      
    