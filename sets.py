#1_____________________________________________________________________________________
kate_sales = {"KitKat" :"34,456,432 US Dollars",
              "Nescafe": "14,106,132 US Dollars",
              "Maggi": "9,960,312 US Dollars",
              "Nido": "44,506,003 US Dollars"}

#2_____________________________________________________________________________________
dalia_sales = {"Lipton":"23,456,000 US Dollars",
               "Breyers": "1,235,891 US Dollars",
               "HellManns":"17,241,412 US Dollars",
               "Marmite": "11,715,324 US Dollars"}

#3_____________________________________________________________________________________
print ("Unilever sales") 
for i in dalia_sales:
    print(i,dalia_sales[i])

#4_____________________________________________________________________________________
print ("Nestle sales")
for i in kate_sales:
    print(i,kate_sales[i])

#5_____________________________________________________________________________________
unilever = 0
nestle = 0
for i in kate_sales:
    nestle+=1
    for b in dalia_sales:
        unilever+=1
        if nestle == unilever:
            print("both companies has the same products number")

#6_____________________________________________________________________________________
nestle_top_sales = "Nido is the top product sales", kate_sales["Nido"]
print (nestle_top_sales)

#7_____________________________________________________________________________________
unilever_top_sales = "Lipton is the top product sales", dalia_sales["Lipton"]

#for questions 8 -10_____________________________________________________________________________________
monica_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
monica_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#8_____________________________________________________________________________________
nestle_unilever_cities = monica_nestle | monica_unilever
print("this is the all the cities that both companies sells in it")
for i in nestle_unilever_cities:
    print(i)

#9_____________________________________________________________________________________
print("these are the common cities that the both companies sells in it")
nestle_unilever = monica_nestle & monica_unilever
for i in nestle_unilever:
    print(i)

#10_____________________________________________________________________________________
print ("this is the cities that Nestle sells in , but Unilver doens't sell in")
cities_nestle_sells_in = monica_nestle - monica_unilever
for i in cities_nestle_sells_in:
    print(i)