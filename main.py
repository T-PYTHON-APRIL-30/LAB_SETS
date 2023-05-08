# Kate -- the sales in US Dollars
nestleSales = {
    "KitKat" : 34456432,
    "Nescafe" : 14106132,
    "Maggi" : 9960312,
    "Nido" : 44506003
}
#--------

# Dalia -- the sales in US Dollars
unileverSales = {
    "Lipton" : 23456000,
    "Breyers" : 1235891,
    "HellManns" : 17241412,
    "Marmite" : 11715324
}
#--------

# Monica -- name of the countries
nestle_cities_sales = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan" }
unilever_cities_sales = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

nestleUnileverCountries = nestle_cities_sales | unilever_cities_sales #Union
nestleUnileverCommon = nestle_cities_sales & unilever_cities_sales #Intersection
nestleCitiesOnly = nestle_cities_sales - unilever_cities_sales #Difference

#--------

# Create a variable to hold the values of Nestle products (use a dicitionary)
nestleProducts = nestleSales.values()
nestleTopSales = max(nestleProducts)
nestleTopProductName = max(nestleSales, key=nestleSales.get) 
nestleTotalSales = sum(nestleProducts)

# Create a variable to hold the values of Unilever products (Use a dictionary)
unileverProducts = unileverSales.values()
unileverTopSales = max(unileverProducts)
unileverTopProductName = max(unileverSales, key=unileverSales.get) 
unileverTotalSales = sum(unileverProducts)


# Print each product sold by Unilever and the sales figures / numbers  for that product.
print()
print("---------- Unilever Sales ----------")
for product , sales in unileverSales.items():
    print(f"The product: {product} \nIt sales: {sales} US Dollars")

# Print each product sold by Nestle and the sales figures / numbers  for that product.
print()
print("---------- Nestle Sales ----------")
for product , sales in nestleSales.items():
    print(f"The product: {product} \nIt sales: {sales} US Dollars")

# Print which of the companies has more products that the other company.
print()
print("---------- More products company ----------")
if len(unileverSales) > len(nestleSales) :
    print("Unilever has more products than Nestle.")
elif len(nestleSales) > len(unileverSales) :
    print("Nestle has more products than Unilever.")
elif len(nestleSales) == len(unileverSales) :
    print("Nestle & Unilever are has the same number of products.")

# Print the top selling product from Nestle with sales figures.
print()
print("---------- Top product in Nestle ----------")
print(f"The top product in Nestle is {nestleTopProductName} with seling {nestleTopSales} US Dollars.")

#  Print the top selling product from Unilever with sales figures.
print()
print("---------- Top product in Unilever ----------")
print(f"The top product in Unilever is {unileverTopProductName} with seling {unileverTopSales} US Dollars.")


# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print()
print("---------- Nestle & Unilever Countries ----------")
print("Nestle & Unilever sales thier products in:")
for city in nestleUnileverCountries:
    print(city,end=" ")
print(".")
# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common
print()
print("---------- Nestle & Unilever Common ----------")
print("The common countries they sells thier products are:")
for city in nestleUnileverCommon:
    print(city,end=" ")
print(".")
# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common
print()
print("---------- Nestle Only ----------")
print("Cities that only sell Nestle products:")
for city in nestleCitiesOnly:
    print(city,end=" ")
print(".")