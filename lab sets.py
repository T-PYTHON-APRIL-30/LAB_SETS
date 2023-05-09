#Kate, Dalia & Monica are work associates . They all work at a consultancy company.

#Kate has the products sales of Nestle :
#KitKat : 34,456,432 US Dollars
#Nescafe : 14,106,132 US Dollars
#Maggi : 9,960,312 US Dollars
#Nido : 44,506,003 US Dollars


#Dalia has the products sales of Unilever :
#Lipton : 23,456,000 US Dollars
#Breyers : 1,235,891 US Dollars
#HellManns : 17,241,412 US Dollars
#Marmite : 11,715,324 US Dollars


#Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:

#Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
#Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


#Using what you've learned during . Please do the following :

#Create a variable to hold the values of Nestle products (use a dicitionary)

nestle_products = {
    "kit kat": 34456432,
    "nescafe": 14106132,
    "maggi": 9960312,
    "nido": 44506003,
}
#Create a variable to hold the values of Unilever products (Use a dictionary)
unilever_prouucts = {
    "Lipton":23456000,
    "Breyers":1235891,
    "HellManns":17241412,
    "Marmite":11715324,
}

#Print each product sold by Unilever and the sales figures / numbers for that product.

print("Unilever Products:")
for products, sales in unilever_prouucts.items():
    print (products+":"+ str(sales) + "US Dollars")


#Print each product sold by Nestle and the sales figures / numbers for that product.

print("\Nestle Products:")
for product, sales in nestle_products.items():
    print(prducts +":" + str(sales) + "US Dollars")

#Print which of the companies has more products that the other company.

if len(nestle_products)>len(unilever_prouucts):
    print("\nNestele has more products than Unilever")
elif len(nestle_products)<len(unilever_prouucts):
    print("\Unilever has more products than Nes(nestle")
else:
    print("\nBpth companies have the same number of products")

#Print the top selling product from Nestle with sales figures.

top_nestle_product =max(nestle_products, key = nestle_products.get)
print("\nTop selling Nestle products:" +top_nestle_product +",Sales" + str(nestle_products[top_nestle_product])"US Dollars")


#Print the top selling product from Unilever with sales figures.

tob_unilever_product = max(unilever_prouucts, key=unilever_prouucts.get)
print("\nTop slling Unilever products: " str+(tob_unilever_products[tob_unilever_product]) + "US Dollars")
      


#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

nestle_cities = set(["Saudi Arabia","Oman", "Kuwait", "Egyot", "Jordan", "Sudan"])
unilever_cities = set(["Saudi Arabis", "Kuwait", "Iraq", " Morocco", "Yemen", "United Emirates"])




#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

common_list = nestle_cities.intersection(unilever_cities)
print("\nCities where both nestle and Unilver sell their products:")
for city in common_cities:
    print(city)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
nestle_only_cities = nestle_cities.difference(unilever_cities)
print("\nCities where only Nestle sells list products:")
for city in nestle_only_cities
   print(city)