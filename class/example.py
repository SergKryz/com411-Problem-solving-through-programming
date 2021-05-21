class Person:

  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln
    self.address = None

  def set_address(self, address):
    self.address = address

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class BankAccount:


  def __init__(self,  ac, sc, owner):
    super().__init__(sc,ac)
    if type(owner) is Person:
      self.owner = owner
    else:
      self.owner = None
    self.balance = 0
  

  def pay_in(self, money):
    self.balance +=money
  
  def withdraw(self, money):
    self.balance -= money


class IndividualAccount(BankAccount):

  def __init__(self,  ac, sc, owner):
    self.sort_code = sc
    self.account_number = ac
    if type(owner) is Person:
      self.owner = owner
    else:
      self.owner = None
    self.balance = 0

  def get_account_data(self):
    print(f" The account belongs to {self.owner}. The acc. nr. is {self.account_number}. The balance is {self.balance}")

  def pay_in(self, money):
    self.balance +=money
  
  def withdraw(self, money):
    self.balance -= money

class SharedAccount(BankAccount):

  def __init__(self, sc, ac, owner):
    #self.sort_code = sc
    #self.account_number = ac
    super().__init__(sc,ac)
    self.owners = []
    self.balance = 0
  
  def pay_in(self, money):
    self.balance +=money
  
  def withdraw(self, money):
    self.balance -= money
#[Piotr, Jane, Luke]
#
  def get_account_data(self):

    f_owners=""

    for person in self.owners:
      f_owners + person + " "

    print(f" The shared account belongs to {f_owners}. The acc. nr. is {self.account_number}. The balance is {self.balance}")


p1 = Person("Piotr", "Bednorz")
# p2 = Person("Daniel", "Grab")
# p3 = Person("Anton", "Peters")
# p4 = Person( "Max", "August")

acc1 = IndividualAccount("12222002", "10-25-55", p1)
# acc2 = IndividualAccount("12345678", "25-85-44", p3)
# acc3 = IndividualAccount("65432100", "45-85-36", p4)

# acc2.get_account_data()
# acc1.get_account_data()


# acc1.pay_in(10)
# acc1.get_account_data()

# acc1.withdraw(30)
# acc1.get_account_data()