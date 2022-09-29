#This is the start of the code, it goes through the first lines before making the text "Welcome to the Cathedral Coffee Club"

print("Welcome to the Cathedral Coffee Club")

#this is printing the menu of available coffee drinks in the store
print("""
Menu

Flat White = 3
Decaf = 3
Cappucino = 3
Latte = 3.5
Hot Chocolate = 4
""")
#This variable sets the value of price to 0 so when the user is finished ordering their drink, the ordered drinks would be placed into the variable "price"
price = 0
#This is the def function that contains the list of the coffee drinks, their prices and the most important one, it can multiply the price of the drink if the user ordered the drink more than once. It also has an else condition if the user wrote an ordered drink 
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


#These strings are triggered after the user inputted their first order, but if they wanted to order more drinks this string will be triggered if the user inputs an Y or yes when prompted if they want to order more drinks

def get_orders():
    next_order = True
    while next_order == True:
      order = input("What drink would you like?: ")
      amount = int(input("How many of these would you like?"))
      check_cost(order, amount)
      next = input("Do you want to order more drinks? Y/N").upper()
      while next != "Y":
         if next == "N":
          next_order = False
          next = "Y" 
         else:
          next = input("That isn't a valid option. Try again")

#This triggers a loop so that it goes back if they want to order more drinks
get_orders()
#This is just a simple string that asks the user if they want sugar along with their order
sugar = input("Would you like sugar with your order?")


#This is an if condition that has a condition oif the price is 0 or is not functioning properly it would print Error and would need to restart the code from the beginning. 
if price == 0:
  print("Order %# Error!")
else:
  print("Your Total amount to pay is ${} for your order. Please pay at the cashier. ".format(price))
  print("Have a good day")
#The code finishes and prints the total amount of price the user would pay how much the order would cost.