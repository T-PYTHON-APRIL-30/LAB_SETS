

# - Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products={34456432:"KitKat" ,14106132:"Nescafe" ,9960312:"Maggi" ,44506003:"Nido"}

# - Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products={23456000:"Lipton",1235891:"Breyers",17241412:"HellManns",
                  11715324:"Marmite"}

# - Print each product sold by Unilever and the sales figures / numbers  for that product.
for k, v in Nestle_products.items():
    print(f"{k} : {v} US Dollars")

print("*****")

# - Print each product sold by Nestle and the sales figures / numbers  for that product.
for k, v in Unilever_products.items():
    print(f"{k} : {v} US Dollars")

print("*****")

# - Print which of the companies has more products that the other company.
if len(Nestle_products) > len(Unilever_products):
    print("the Nestle company has more product than the Unilever company")
elif len(Unilever_products) > len(Nestle_products):
        print("the Unilever company has more product than the Nestle company")
else:
     print("the two companys have the same number of products")
print("*****")

# - Print the top selling product from Nestle with sales figures.
for k ,v in Nestle_products.items():
     print("the top selling product from Nestle is:",v,"with sales figures=", max(Nestle_products))
     break
print("*****")
# - Print the top selling product from Unilever with sales figures.
for k ,v in Unilever_products.items():
     print("the top selling product from Unilever is:",v,"with sales figures=", max(Unilever_products))
     break
print("*****")
# - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle_countries ={ "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_countries ={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for countries in Nestle_countries.union (Unilever_countries):
     print (countries)

print("*****")

# - Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print ( "the cities that both Nestle & Unilver sell in common are:")
for countries in Nestle_countries.intersection (Unilever_countries):
    print(countries)

print("*****")
# - Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print ( "the cities that  Nestle sells in , but Unilver doens't sell in are:")
for countries in Nestle_countries.difference (Unilever_countries):
    print(countries)