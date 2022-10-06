class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.available_funds = 0


  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
    self.available_funds += float(amount)
    #no return?


  def withdraw(self, amount, description=''):
    neg_amount= amount*-1
    if self.check_funds(amount):
      self.ledger.append({'amount': neg_amount, 'description': description})
      self.available_funds += float(neg_amount)
      return True
    else: 
      return False


  def get_balance(self):
    # gets the balance from the summation of the withdrawals and deposits in ledger, returns the balance in numerical format
    return self.available_funds


  def transfer(self,amount,destination_cat):
    if self.check_funds(amount):
      self.withdraw(amount, description=f'Transfer to {destination_cat.name}')
      destination_cat.deposit(amount, description=f'Transfer from {self.name}')
      return True
    else: 
      return False
    pass
  

  def check_funds(self,amount):
    #compairs the difference between the total from the ledger and the amount provided.
    if self.available_funds >= amount:
      #print(f'You have {self.available_funds} the amount you are checking against is {amount}')
      return True
    else:
      #print(f' {self.available_funds} is not enough for the amount of {amount}')
      return False
    


  def __repr__(self):
    return f'******* {self.name} ********'
    #placeholder for testing, supposed to be an exact string with 30 characters and self.name centered
    #also a list of the items in the ledger, each line should show the description and amaount.
    #a line with the total.



### outside of class
def create_spend_chart(list_cats):
  return f'string that is a bar chart'

