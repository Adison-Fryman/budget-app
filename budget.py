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
    title = str(self.name).center(30, '*') + '\n'

    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:7.2f}" + '\n'
      total += item['amount']
    return title + items + 'Total: ' + str(total)


### outside of class
#def create_spend_chart(list_cats):
  #return f'string that is a bar chart'

  # this last item is a project in itself, that I feel several while and for loops can account for with significant formating. My time is better served learning SQL and Tableau...sorry codecamp




