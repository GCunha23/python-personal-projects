"""
Author: Gonçalo Cunha (GitHub: GCunha23)
Date Created: 10/01/2025
Last Modified: 10/01/2025

Description:
This is a simple supermarket cashier program.
"""

# Defines a function to get the products and quantities
# The Cashier inputs all the products bought one by one
# That info is stored in a dictionary called "buyingData" and returns back

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ")
        if details == "A":
            product = input("Enter product: ")
            quantity = int(input("Enter quantity: "))
            buyingData.update({product:quantity})
        elif details == "Q":
            enterDetails = False
        else:
            print("Please select a correct option")
    return buyingData

# This function gives the subtotal of a single product as per its price and quantity mentioned

def getPrice(product,quantity):
    priceData = {
        "Biscuit":3,
        "Chicken":5,
        "Egg":1,
        "Fish":3,
        "Coke":2,
        "Bread":2,
        "Apple":3,
        "Onion":3
    }
    subtotal = priceData[product] * quantity
    print(product + ":$" + str(priceData[product]) + "x" + str(quantity) + "=" + str(subtotal))
    return subtotal

# Defines a function for the discount
# It is decided if the discount is applicable or not, given the total bill amount

def getDiscount(billAmount,membership):
    discount = 0
    if billAmount >= 25:
        if membership == "Gold":
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == "Silver":
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == "Bronze":
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + "% off for " + membership + " " + "membership on total ammount: $" + str(billAmount))
    else:
        print("No discount on amount less then $25")
    return billAmount

# Defines a function for the final bill
# A loop is created to call getPrice() function until the subtotal is added for all the products within buyingData, and then calls getDiscount() function to calculate discounted amount

def makeBill(buyingData,membership):
    billAmount=0
    for key,value in buyingData.items():
        billAmount += getPrice(key,value)
    billAmount = getDiscount(billAmount,membership)
    print("The discounted amount is $" + str(billAmount))

# This is the main part of the program which is not inside any function
# The first line of execution of code will start from here

buyingData = enterProducts() # Calls function
membership = input("Enter customer membership: ")
makeBill(buyingData,membership) # Calls function