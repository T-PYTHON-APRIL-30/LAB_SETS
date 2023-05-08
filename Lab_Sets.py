'''Kate, Dalia & Monica are work associates . They all work at a consultancy company.
Kate has the products sales of Nestle :
KitKat : 34,456,432 US Dollars
Nescafe : 14,106,132 US Dollars
Maggi : 9,960,312 US Dollars
Nido : 44,506,003 US Dollars'''

'''Dalia has the products sales of Unilever :
Lipton : 23,456,000 US Dollars
Breyers : 1,235,891 US Dollars
HellManns : 17,241,412 US Dollars
Marmite : 11,715,324 US Dollars'''

'''Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"'''

'''Using what you've learned during . Please do the following :
*Create a variable to hold the values of Nestle products (use a dicitionary)
*Create a variable to hold the values of Unilever products (Use a dictionary)
*Print each product sold by Unilever and the sales figures / numbers for that product.
*Print each product sold by Nestle and the sales figures / numbers for that product.
*Print which of the companies has more products that the other company.
*Print the top selling product from Nestle with sales figures.
*Print the top selling product from Unilever with sales figures.
*Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
*Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
*Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.'''

def displayProducts(productDict:dict):
    for key, value in productDict.items():
        print(f'The sales number for {key} is ${value}')


def topSellingProducts(prodctDict:dict):
    top = 0
    product = ''
    for key, value in prodctDict.items():

        if int(value) > top:
            top = int(value)
            product = key


    print(f'{product} with sales figures ${top}')





nestle_products = {'KitKat':'34456432','Nescafe':'14106132','Maggi':'9960312','Nido':'44506003'}
unilever_products = {'Lipton':'23456000','Breyers':'1235891','HellManns':'17241412','Marmite':'11715324'}

nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print('Nestle Products:')
displayProducts(nestle_products)

print()

print('Unilever Products:')
displayProducts(unilever_products)

print()

if len(nestle_products) > len(unilever_products):
    print('Nestle products has more products than Unilever')

elif len(nestle_products) < len(unilever_products):
    print('Unilever products has more products than Nestle')

else:
    print('The both companies has the same number of products.')

print()



print('The top selling product in Nestle is:')
topSellingProducts(nestle_products)
print()
print('The top selling product in Unilever is:')
topSellingProducts(unilever_products)

print()

#Union
print('all the cities Unilever & Nestle sell their products in are: ')
cities_set = set()
for city1 in nestle_set:
    for city2 in unilever_set:
        if city1 != city2:
            cities_set.add(city1)
            cities_set.add(city2)
    
print(cities_set)

print()

#Intersection
print('The cities that both Nestle & Unilver sell in common are: ')
cities_set2 = set()
for city1 in nestle_set:
    for city2 in unilever_set:
        if city1 == city2:
            cities_set2.add(city2)
    
print(cities_set2)


print()

#Difference:
print('The cities Nestle sells in , but Unilver doens\'t sell in are: ')
cities_set3 = set()
for city1 in nestle_set:
    for city2 in unilever_set:
        if city1 not in unilever_set:
            cities_set3.add(city1)
    
print(cities_set3)
        






