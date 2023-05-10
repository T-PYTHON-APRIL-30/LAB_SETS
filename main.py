nestle_products = {
    "KitKat": "34456432",
    "Nescafe": "14106132",
    "Maggi": "9960312",
    "Nido": "44506003"
}
unilever_products = {
    "Lipton" : "23456000",
    "Breyers" : "1235891",
    "HellManns" : "17241412",
    "Marmite" : "11715324"
}
nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

def formating(number):
    return ("{:,}".format(number))


def disply(products):
    i: int = 1
    for product in products:
        print(f"{i}. {product} {formating(int(products[product]))} US Dollars")
        i += 1
    print("\n")


def disply_top(products):
    top_sell = max(products)
    print(f"{top_sell}: {formating(int(products[top_sell]))} US Dollars")
    print("\n")


print("Unilever products:")
disply(unilever_products)

print("Nestle products:")
disply(nestle_products)

if len(nestle_products) > len(unilever_products):
    print("Nestle has more products than Unilever.")
    print("\n")
elif len(nestle_products) == len(unilever_products):
    print("Nestle and Unilever has the same products amount.")
    print("\n")
else:
    print("Unilever has more products than Nestle.")
    print("\n")


print("The top selling product from Nestle:")
disply_top(nestle_products)

print("The top selling product from Unilever:")
disply_top(unilever_products)

union = unilever_countries | nestle_countries
intersection = unilever_countries & nestle_countries
difference = nestle_countries - unilever_countries

print("All cities that Unilever and Nestle selling their products in:")
for country in union:
    print(country)


print("\n")
print("Unilever and Nestle sell their products in:")
for country in intersection:
    print(country)


print("\n")
print("Cities that Nestle sells in, but Unilver doens't sell in:")
for country in difference:
    print(country)