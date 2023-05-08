'''
Create a variable to hold the values of Nestle products (use a dicitionary)
Create a variable to hold the values of Unilever products (Use a dictionary)
Print each product sold by Unilever and the sales figures / numbers for that product.
Print each product sold by Nestle and the sales figures / numbers for that product.
Print which of the companies has more products that the other company.
Print the top selling product from Nestle with sales figures.
Print the top selling product from Unilever with sales figures.
Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''
kate_sales_of_Nastle = {
    "34,456,432": "KitKat",
    "14,106,132 ": "Nescafe",
    "9,960,312": "Maggi",
    "44,506,003": "Nido",
}
Dalia_sales_of_unilever  = {
    "23,456,000": "Lipton",
    "1,235,891 ": "Breyers",
    "17,241,412": "HellManns",
    "11,715,324": "Marmite"
}

currncy="US Dollars"

print(kate_sales_of_Nastle)
print("--"*14)

print(Dalia_sales_of_unilever)
print("--"*14)

#Print the top selling product from Nestle
top_selling_Nastle = max(kate_sales_of_Nastle, key = kate_sales_of_Nastle.get)
print("top selling product from Nestle:", top_selling_Nastle, "is:", kate_sales_of_Nastle[top_selling_Nastle], currncy)
print("--"*14)

# Print the top selling product from Unilever
top_selling_unilever = max(Dalia_sales_of_unilever, key = Dalia_sales_of_unilever.get)
print("top selling product from Nestle Unilever:", top_selling_unilever, "is:", Dalia_sales_of_unilever[top_selling_unilever], currncy)
print("--"*14)

# Using Sets & a loop, print all the cities Nestle sell their products in
print("cities Nestle sell their products in:")
for city in kate_sales_of_Nastle:
    print(city + currncy)
# Using Sets & a loop, print all the cities Unilever sell their products in
print("--"*14)

print("cities Unilever sell their products in:")
for city in Dalia_sales_of_unilever:
    print(city + currncy)
# second part    
print("--"*14)

Monica_Set_contry_Nstle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Monica_Set_contry_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in
Monica_Set_contry_Nstle_unilever = Monica_Set_contry_unilever | Monica_Set_contry_Nstle
print(Monica_Set_contry_Nstle_unilever)
print("--"*14)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common
Monica_Set_contry_Nstle_unilever1 = Monica_Set_contry_unilever & Monica_Set_contry_Nstle
print(Monica_Set_contry_Nstle_unilever1)
print("--"*14)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in
Monica_Set_contry_Nstle_unilever2 = Monica_Set_contry_Nstle - Monica_Set_contry_unilever
print(Monica_Set_contry_Nstle_unilever2)
print("--"*14)