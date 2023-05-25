#1Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products = {34456432 : "KitKat", 14106132 : "Nescafe", 9960312  : "Maggi", 44506003 : "Nido"}
#2Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products ={23456000: "Lipton", 1235891 : "Breyers", 17241412 : "HellManns", 11715324: "Marmite"}
#3Print each product sold by Unilever and the sales figures / numbers for that product.
for sales ,product in Unilever_products.items():
    print(f"sales numbers {sales} product sold by Unilever:{product}")
print("--------------------------------------------------------")
#4Print each product sold by Nestle and the sales figures / numbers for that product.
for sales ,product in Nestle_products.items():
    print(f"sales numbers {sales} product sold by Nestle:{product}")
print("--------------------------------------------------------")
#5Print which of the companies has more products that the other company.
lenNestle =(len(Nestle_products))
lenUnilever =(len(Unilever_products))
if lenUnilever>lenNestle:
    print("Unilever companies has more products that the Nestle company. ")
    if lenNestle>lenUnilever:
     print("Nestla companies has more products that the Nestle company. ")
else:
    print("each Companys have same number of product")
print("--------------------------------------------------------")
#Print the top selling product from Nestle with sales figures.
for product ,sales in Nestle_products.items():
    print(f"product sold by Nestle: {sales} sales numbers{product}")

########6Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products ={23456000: "Lipton", 1235891 : "Breyers", 17241412 : "HellManns", 11715324: "Marmite"}
#7Print which of the companies has more products that the other company.
lenUnilever =(len(Unilever_products))
if lenUnilever>lenNestle:
    print("Unilever companies has more products that the Nestle company. ")
    if lenNestle>lenUnilever:
     print("Unilever companies has more products that the Nestle company. ")
else:
    print("each Companys have same number of product")
#8Print the top selling product from Nestle with sales figures.
Key_max = max(zip(Nestle_products.values(), Nestle_products.keys()))[1]  
print("The key with the maximum value is: ", Key_max)  
#9Print the top selling product from Unilever with sales figures.
Key_max = max(zip(Unilever_products.values(), Unilever_products.keys()))[1]  
print("The key with the maximum value is: ", Key_max)
#10Using Sets & a loop, print all the cities Nestle.
cities_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
for key in cities_Nestle:
    print(key)
#10Using Sets & a loop, print all the cities Unilever.
cities_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
for key in cities_Unilever:
    print(key)
#11Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
c = (cities_Nestle & cities_Unilever)
for i in  c:
   print(i)
#12Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
c=(cities_Nestle - cities_Unilever)
for i in  c:
   print(i)