'''
# LAB_SETS


### Kate, Dalia & Monica are work associates . They all work at a consultancy company.

## Kate has the products sales of Nestle :

##### KitKat : 34,456,432 US Dollars
##### Nescafe : 14,106,132 US Dollars
##### Maggi : 9,960,312 US Dollars
##### Nido : 44,506,003 US Dollars

      

## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars
      

## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.
- Print the top selling product from Nestle with sales figures.
- Print the top selling product from Unilever with sales figures.
- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''
#Create a variable to hold the values of Nestle products (use a dicitionary)
nestleProducts : dict = {
    "KitKat" : 34456432,
    "Nescafe" : 14106132,
    "Maggi" : 9960312,
    "Nido" : 44506003
}
#Create a variable to hold the values of Unilever products (Use a dictionary)
unileverProducts : dict = {
    "Lipton" : 23456000,
    "Breyers" : 1235891,
    "HellManns" : 17241412,
    "Marmite" : 11715324
}

def printProduct(dictionary : dict, message : str = "US Dollars"):
    for product, sale in dictionary.items():
        print(f"{product} : {sale} {message}")
#Print each product sold by Unilever and the sales figures / numbers  for that product.
print("the Unilever Prodect sold: ")
printProduct(unileverProducts)
print("\n", "----"*15, "\n")
#Print each product sold by Nestle and the sales figures / numbers  for that product.
print("the Nestle Prodect sold: " , len(nestleProducts))
printProduct(nestleProducts)
print("\n", "----"*15, "\n")
#Print which of the companies has more products that the other company.
if len(nestleProducts) > len(unileverProducts):
    print("the Nestle company has more product then Unilever company")
elif len(nestleProducts) < len(unileverProducts):
    print("the Unilever company has more product then Nestle company")
else:
    print("all of them have the same quantity product")
print("\n", "----"*15, "\n")
def searchMax(dictionary : dict) :
    top : int = 0
    productName : str = ""
    for product, salse in dictionary.items():
        if salse > top :
            top = salse
            productName = product
    printProduct(dictionary= {productName : top})

#Print the top selling product from Nestle with sales figures.
print("the top selling product from Nestle: ", end=" ")
searchMax(nestleProducts)
print("\n", "----"*15, "\n")
#Print the top selling product from Unilever with sales figures.
print("the top selling product from Unilever: ", end=" ")
searchMax(unileverProducts)
print("\n", "----"*15, "\n")
#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
nestlecities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilevercities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

def printSet(cities : set):
    for city in cities:
        print(city)


print("All the cities Unilever & Nestle sell their products in: ")
printSet(nestlecities.union(unilevercities))
print("\n", "----"*15, "\n")
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("The cities that both Nestle & Unilver sell in common: ")
printSet(nestlecities.intersection(unilevercities))
print("\n", "----"*15, "\n")
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in
print("The cities Nestle sells in , but Unilver doens't sell in: ")
printSet(nestlecities.difference(unilevercities))
print("\n", "----"*15, "\n")
