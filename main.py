"""
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


"""

values_of_Nestle={
    "KitKat" : 34456432,
    "Nescafe" : 14106132, 
    "Maggi" : 9960312,
    "Nido" : 44506003
}

values_of_Unilever={
    "Lipton" : 23456000,
    "Breyers" : 1235891,
    "HellManns" : 17241412,
    "Marmite" : 11715324
}
print("products sales of Nestle")
for product,sales in values_of_Nestle.items():
    print(f"Products Name is: {product} and sales: {sales} US Dollars")

print("\nproducts sales of Unilever")
for product,sales in values_of_Unilever.items():
    print(f"Products Name is: {product} and sales: {sales} US Dollars")

if len(values_of_Nestle) > len(values_of_Unilever):
    print("\nNestle has more products than Unilever.")
elif len(values_of_Nestle) < len(values_of_Unilever):
    print("\nUnilever has more products than Nestle.")
else:
    print("\nBoth companies have an equal number of products.")


# Print the top selling product from Nestle with sales figures.

top_selling_nestle=0
for product,sales in values_of_Nestle.items():
    if  sales> top_selling_nestle:
        top_selling_nestle=sales
        top_product=product
print(f"\nThe top selling Nestle product is {top_product} with {top_selling_nestle} US Dollars in sales.")



top_selling_unilevr=0
for product,sales in values_of_Unilever.items():
    if  sales > top_selling_unilevr:
        top_selling_unilevr=sales
        top_product_unilever=product
print(f"\nThe top selling Unilever product is {top_product_unilever} with {top_selling_unilevr} US Dollars in sales.")

Nestle_cities= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


all_the_cities_Unilever_Nestle = Nestle_cities | Unilever_cities

cities_that_both_Nestle_Unilver_sell_in_common = Nestle_cities & Unilever_cities

the_cities_Nestle_sells_in_but_Unilver_doenst_sell_in = Nestle_cities - Unilever_cities

print("\nall the cities Unilever & Nestle sell their products in:")
for city in all_the_cities_Unilever_Nestle:
    print(city)

print("\nthe cities that both Nestle & Unilver sell in common:")
for city in cities_that_both_Nestle_Unilver_sell_in_common:
    print(city)

print("\nthe cities Nestle sells in , but Unilver doens't sell in:")
for city in the_cities_Nestle_sells_in_but_Unilver_doenst_sell_in:
    print(city)