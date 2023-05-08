
nestle_products_sales = {"KitKat":34456432, "Nescafe":14106132, "Maggi":9960312, "Nido":44506003}
unilever_products_sales = {"Lipton":23456000, "Breyers":1235891, "HellManns":17241412, "Marmite":11715324}

nestle_location = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_location = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Print each product sold by Nestle and the sales figures / numbers for that product.
print("\nNestle product sales: ")
for product, numbers in nestle_products_sales.items():
    print(product, numbers)

#Print each product sold by Unilever and the sales figures / numbers for that product.
print("\nUnilever product sales: ")
for product, numbers in unilever_products_sales.items():
    print(product, numbers)

#Print which of the companies has more products than the other company.
if nestle_products_sales.keys() > unilever_products_sales.keys():
    print("Nestle has more products than Unilever")
elif nestle_products_sales.keys() < unilever_products_sales.keys():
    print("Unilever has more products than Nestle")
else:
    print("\nBoth companies has equal number of product")

#Print the top selling product from Nestle with sales figures.
print("\nTop selling product in Nestle:")
nestle_top_value = max(nestle_products_sales.values())
nestle_top_key = max(nestle_products_sales, key=nestle_products_sales.get)
print(nestle_top_key, nestle_top_value)

#Print the top selling product from Unilever with sales figures.
print("\nTop selling product in unilever:")
unilever_top_value = max(unilever_products_sales.values())
unilever_top_key = max(unilever_products_sales, key=unilever_products_sales.get)
print(unilever_top_key, unilever_top_value)

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("\nCities Unilever & Nestle sell their products in: ")
union_locations= nestle_location | unilever_location
for cities in union_locations:
    print(cities)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("\nCities that both Nestle & Unilver sell in common: ")
intersection_locations= nestle_location & unilever_location
for cities in intersection_locations:
    print(cities)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("\nCities Nestle sells in , but Unilver doens't sell in: ")
difference_locations = nestle_location - unilever_location
for cities in difference_locations:
    print(cities)

