#list of items sold by the cafe called menu
menu = ['coke','coffee','tea','cookie','sandwich','cake']

#dictionary that stores the stock level of each item called stock
stock = {
    'coke': 40,
    'coffee': 25,
    'tea': 25,
    'cookie': 15,
    'sandwich': 10,
    'cake': 5
}
#dictionary that store the price of each item called price
price = {
    'coke': 13,
    'coffee': 20,
    'tea': 20,
    'cookie': 15,
    'sandwich': 25,
    'cake': 30
}

# Create a dictionary to store item values, which would be calulated by multiplying the stock and price of the item.
item_values = {}

# Loops through each item in the menu list to be calculated
for item in menu:
    # Calculate the item_value for  the total cost of each item
    item_value = stock[item] * price[item]
    # Store the item_value in the dictionary with the item as the key
    item_values[item] = item_value

# Displays the items from the menu with the total value calculated from the stock and price
print(f"Total stock value of each item:\n{item_values}")
print("==========================================")
#stores the total stock worth in the cafe
total_stock = 0
#loops throught each item in the item_values dictionary
for item_value in item_values.values():
    #adds the value of each item in the dictionary to the totalstock
    total_stock += item_value
print(f"Total Stock: £{total_stock}")

