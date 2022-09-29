#This is the start of the code, it goes through the first lines before making the text "Welcome to the Cathedral Coffee Club"

print("Welcome to the Cathedral Coffee Club")
#this is printing the menu of coffee drinks in the store
print("""
Menu:
Flat White = 3
Decaf = 3
Cappucino = 3
Latte = 3.5
Hot Chocolate = 4""")
#This variable sets the value of price to 0 so when the user is finished ordering their drink, the math would check out
price = 0
#This is the start of one of the defining functions that set 
def check_cost(drink, amount):
  drink = drink.lower()  
  global price
  if drink == "flat white" or drink == "cappucino" or drink == "decaf":
    price += 3 * amount
  elif drink == "latte":
    price += 3.5 * amount
  elif drink == "hot chocolate":
    price += 4 * amount
  else:
    print("Not a valid order")


#These strings and values take the order name and what the price of the coffee the user selected

def get_orders():
    next_order = True
    while next_order == True:
      order = input("What is your order?: ")
      amount = int(input("How many of these would you like?"))
      check_cost(order, amount)
      next = input("Do you want to order more drinks? Y/N").upper()
      while next != "Y":
         if next == "N":
          next_order = False
          next = "Y"
         else:
          next = input("That isn't a valid option. Try again")


get_orders()

sugar = input("Would you like sugar with your order?")


#set different function here that will loop back to a next 
#set an if condition incase the user wont put the 2nd order as empty set it as - so it would not affect the final price
if price == 0:
  print("Order %# Error")
else:
  print("Have a good day")
print("Your Total amount to pay is ${} ".format(price))
