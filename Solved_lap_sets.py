Nestle_product = {"KitKat": "34,456,432",
                   "Nescafe": "14,106,132",
                   "Maggi": "9,960,312",
                   "Nido": "44,506,003"
                   }

Unilever_product = {"Lipton": '23,456,000',
                    "Breyers": "1,235,891",
                    "HellManns": "17,241,412",
                    "Marmite": "11,715,324"
                    }

for a in Unilever_product:
    print(a,end=" ")
    print(Unilever_product[a],"US Dolar")

print("___"*20)
print()

for b in Nestle_product:
    print(b, end=" ")
    print(Nestle_product[b],"US Dolar")


print("___"*20)
print()

#wich companies has more product
number_of_products_n = 0
number_of_products_u = 0
for a in Nestle_product:
    number_of_products_n += 1

for a in Unilever_product:
    number_of_products_u += 1

if number_of_products_n > number_of_products_u:
    print("Nestle has more product")
elif number_of_products_n < number_of_products_u:
    print("Unilever has more product")
else:
    print("the companies has same number of products")

print("___"*20)
print()

#print top selling

key_n = max(Nestle_product)
print("Largest selles of Nestle:",key_n,Nestle_product[key_n])

key_u = max(Unilever_product)
print("Largest selles of Unilever:",key_u,Unilever_product[key_u])

print("___"*20)
print()

#using sets and loop

Nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for a in Nestle_cities:
    print(a)

print("___"*20)

for b in Unilever_cities:
    print(b)

print("___"*20)
print()

#print cities common

both_cities = Nestle_cities.intersection(Unilever_cities)
for a in both_cities:
    print(a)

print("___"*20)
print()

#print cities nestle sells and unilever doesn't sells

Nestle_cities_only = Nestle_cities.difference(Unilever_cities)
for b in Nestle_cities_only:
    print(b)
