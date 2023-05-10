'''
LAB_SETS
Kate, Dalia & Monica are work associates . They all work at a consultancy company.
Kate has the products sales of Nestle :
KitKat : 34,456,432 US Dollars
Nescafe : 14,106,132 US Dollars
Maggi : 9,960,312 US Dollars
Nido : 44,506,003 US Dollars
Dalia has the products sales of Unilever :
Lipton : 23,456,000 US Dollars
Breyers : 1,235,891 US Dollars
HellManns : 17,241,412 US Dollars
Marmite : 11,715,324 US Dollars
Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"
Using what you've learned during . Please do the following :
Create a variable to hold the values of Nestle products (use a dicitionary)
Create a variable to hold the values of Unilever products (Use a dictionary)
Print each product sold by Unilever and the sales figures / numbers for that product.
Print each product sold by Nestle and the sales figures / numbers for that product.
Print which of the companies has more products that the other company.
Print the top selling product from Nestle with sales figures.
Print the top selling product from Unilever with sales figures.
Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.'''

Nestle_products ={
    "KitKat" : 34456432, 
    "Nescafe" : 14106132,
    "Maggi" : 9960312,
    "Nido" : 44506003
}
Unilever_products={
    "Lipton" : 23456000,
    "Breyers" : 1235891,
    "HellManns" : 17241412,
    "Marmite" : 11715324
}
Nestle_cities= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("Producs of Nestle:")
for key1 in Nestle_products:
    print(f"{key1}: {Nestle_products[key1]} US Dollars")

print("Products of Unilever:")
for key2 in Unilever_products:
    print(f"{key2}: {Unilever_products[key2]} US Dollars")



def best_seling_products(company1 : dict,company2: dict)->dict:
    sum1 =0
    sum2=0
    for values in company1:
        sum1+=company1[values]

    for values2 in company2:
        sum2+=company2[values2]
    if sum1 > sum2:
        return company1
    elif sum2 > sum1:
        return company2
    
def comparing_element(company1:dict,company2:dict):
    length1= len(company1)
    lenght2=len(company2)
    if length1>lenght2:
        return company1
    elif lenght2>length1:
        return company2
    
if comparing_element(Nestle_products,Unilever_products) == Nestle_products:
    print(f"The company ha more element is: Nestle")
else:
    print("The company ha more element is: Unilever")
    
if best_seling_products(Nestle_products,Unilever_products) == Nestle_products:
    print(f"The company has more products is: Nestle")
else:
    print(f"The company has more products is: Unilever")

def top_products(company:dict):

    largest_number=0
    for value1 in company:
        if largest_number < company[value1]:
            largest_number= company[value1]
            top= value1
    return top

print(f"The top product in Nestle is: {top_products(Nestle_products)}")
print(f"The top product in Unilever is: {top_products(Unilever_products)}")

print("All the cities Unilever & Nestle sell their products in:")
cities_union= Nestle_cities.union(Unilever_cities)
for value1 in cities_union:
    print(value1)

print("The cities that both Nestle & Unilver sell in common: ")
cities_intersection= Nestle_cities.intersection(Unilever_cities)
for value2 in cities_intersection:
    print(value2)

print("The cities Nestle sells in , but Unilver doens't sell in: ")
cities_difference= Nestle_cities.difference(Unilever_cities)
for value3 in cities_difference:
    print(value3)
