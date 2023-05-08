'''
Create a variable to hold the values of Nestle products (use a dicitionary)
Create a variable to hold the values of Unilever products (Use a dictionary)
Print each product sold by Unilever and the sales figures / numbers for that product.
Print each product sold by Nestle and the sales figures / numbers for that product.
Print which of the companies has more products that the other company.
Print the top selling product from Nestle with sales figures.
Print the top selling product from Unilever with sales figures.
Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''

# Create a variable to hold the values of Nestle products
nestle_products = {
    "KitKat": 34456432,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003,
}

# Create a variable to hold the values of Unilever products
unilever_products = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324,
}

# Print each product sold by Unilever and the sales figures / numbers for that product
print("Unilever products:")
for product, sales in unilever_products.items():
    print(f"{product}: {sales} US Dollars")

# Print each product sold by Nestle and the sales figures / numbers for that product
print("\nNestle products:")
for product, sales in nestle_products.items():
    print(f"{product}: {sales} US Dollars")

# Print which of the companies has more products than the other company
if len(nestle_products) > len(unilever_products):
    print("\nNestle has more products.")
elif len(nestle_products) < len(unilever_products):
    print("\nUnilever has more products.")
else:
    print("\nBoth companies have the same number of products.")

# Print the top selling product from Nestle with sales figures
top_nestle_product = max(nestle_products, key=nestle_products.get)
print(f"\nTop selling product from Nestle: {top_nestle_product} with {nestle_products[top_nestle_product]} US Dollars")

# Print the top selling product from Unilever with sales figures
top_unilever_product = max(unilever_products, key=unilever_products.get)
print(f"\nTop selling product from Unilever: {top_unilever_product} with {unilever_products[top_unilever_product]} US Dollars")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in
nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

all_countries = nestle_countries.union(unilever_countries)
print("\nAll countries Unilever & Nestle sell their products in:")
for country in all_countries:
    print(country)

# Using Sets & a loop, print the cities that both Nestle & Unilever sell in common
common_countries = nestle_countries.intersection(unilever_countries)
print("\nCountries both Nestle & Unilever sell in common:")
for country in common_countries:
    print(country)

# Using Sets & a loop, print the cities Nestle sells in, but Unilever doesn't sell in
nestle_only = nestle_countries.difference(unilever_countries)
print("\nCountries Nestle sells in, but Unilever doesn't:")
for country in nestle_only:
    print(country)
