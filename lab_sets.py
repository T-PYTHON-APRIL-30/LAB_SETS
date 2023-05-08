# LAB_SETS


# Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle = {
    "KitKat": 34456432,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003
}

# Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324
}

# Print each product sold by Nestle and the sales figures / numbers  for that product.
print(Nestle)

# Print each product sold by Unilever and the sales figures / numbers  for that product.
print(Unilever)

# Print which of the companies has more products that the other company.
if Unilever.__len__() > Nestle.__len__():
    print("Unilever has more products than Nestle")
elif Nestle.__len__() > Unilever.__len__():
    print("Nestle has more products than Unilever")
else:
    print("Both companies sell the same ammount of products")

# Print the top selling product from Nestle with sales figures.
top_seller = max(Nestle.values())
top_key = list(Nestle.keys())[list(Nestle.values()).index(top_seller)]
print(f"the top sellting Item is: {top_key} with {top_seller} US Dollars")

# Print the top selling product from Unilever with sales figures.
top_seller = max(Unilever.values())
top_key = list(Unilever.keys())[list(Unilever.values()).index(top_seller)]
print(f"the top sellting Item is: {top_key} with {top_seller} US Dollars")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
nestle_cities = set()
nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities = set()
unilever_cities = {"Saudi Arabia", "Kuwait",
                   "Iraq", "Morocco", "Yemen", "United Emirates"}
all_cities = nestle_cities | unilever_cities
print(all_cities)

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
incommon_cities = nestle_cities & unilever_cities
print(incommon_cities)

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
nestle_cities_only = nestle_cities-unilever_cities
print(nestle_cities_only)
