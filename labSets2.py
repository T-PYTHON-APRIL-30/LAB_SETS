
Nestle_products = {34456432 : "KitKat", 14106132 : "Nescafe", 9960312  : "Maggi", 44506003 : "Nido"}

Unilever_products ={23456000: "Lipton", 1235891 : "Breyers", 17241412 : "HellManns", 11715324: "Marmite"}

for sales , product in Unilever_products.items():
   print(f"Unilever's {product} sales figure is: {sales}$")

print("--")

for sales , product in Nestle_products.items():
    print(f"Nestle's {product} sales figure is: {sales}$")

print("--")

lenOfNest = len(Nestle_products)
lenOfUnil = len(Unilever_products)
if lenOfUnil>lenOfNest:
    print("Unilever companies have more products than Nestle companies. ")
elif lenOfNest>lenOfUnil:
     print("Nestla companies have more products than Unilever companies. ")
else:
    print("Companies have the same number of products")

print("--")

highest_product_nestle = max(zip(Nestle_products.values(), Nestle_products.keys()))[1]  
print(f"Nestle's highest product value: {highest_product_nestle}$")  
highest_product_Unilever = max(zip(Unilever_products.values(), Unilever_products.keys()))[1]  
print(f"Unilever's highest product value: {highest_product_Unilever}$")

print("--")

citiesNis = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
for city in citiesNis:
    print(city)
print ("--")
citiesUni = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
for city in citiesUni:
    print(city)
print("--")
for city in citiesUni & citiesNis:
    print(city)
print("--")
for city in citiesNis - citiesUni:
    print(city)