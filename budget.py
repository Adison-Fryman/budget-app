class Category:
  def __init__(self, name, ledger, available_funds = 0):
    self.name = name
    self.ledger = ledger
    self.available_funds = available_funds
    
  def deposit(self, amount, description=''):
    self.ledger += {"amount": amount, "description": description}
    pass

  def withdraw(self, amount, description=''):
    if #value of check_funds is > than amount
      self.ledger += {"amount": (amount*-1), "description": description}
      return True
    else: 
      return False
    pass

  def get_balance(self):
    # gets the balance from the sumation of the withraws and deposits, returns the balance numerical
    pass

  def transfer(self,amount, source_cat, description = ''):
    description = f'Transfer from {source_cat}'
    if #value of check_funds is > than amount
      self.withdraw(amount, description)
      return True
    else: 
      return False
    pass
  

  def check_funds(self,amount)
    #confused what is the differnce between get balance and check funds. looks to be the output
    if get_balance>=amount
      return True
    else:
      return False
    
    pass

  def __repr__(self):
    return f'A title line of 30 characters where the {self.name} of the category is centered in a line of * characters.' 
    #also a list of the items in the ledger, each line should show the description and amaount.
    #a line with the total.



  def create_spend_chart(categories):
  
  
### outside of class
def create_spend_chart(list_cats):
  return f'string that is a bar chart'

