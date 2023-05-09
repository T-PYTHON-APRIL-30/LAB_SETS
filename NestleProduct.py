'''LAB_SETS
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
#Create a variable to hold the values of Unilever products (Use a dictionary)
kateProducts={("KitKat","34,456,432"),("Nescafe","14,106,132"),("Maggi","9,960,312"),("Nido","44,506,003")}
DailaProducts={("Lipton","23,456,000"),("Breyers","1,235,891"),("HellManns","17,241,412"),("Marmite","11,715,324")}
NestleDec={"Saudi Arabia":0, "Oman":1, "Kuwait":2, "Egypt":3, "Jordan":4, "Sudan":5}
UnileverDec={"Saudi Arabia":0, "Kuwait":2, "Iraq":6, "Morocco":7, "Yemen":8, "United Emirates":9}
def NumOfProduct(product=kateProducts[]):
    for i in product.items():
      if product:
         i+=1
         numProd=i
         return numProd
#Print each product sold by Unilever and the sales figures / numbers for that product.       
print(f"{kateProducts}US Dollars/{NumOfProducts(kateProducts[i])}.")
#Print each product sold by Nestle and the sales figures / numbers for that product.
print(f"{DailaProducts}US Dollars/{NumOfProduct(product)}.")
#Print which of the companies has more products that the other company.

if Len(kateProducts)==len(DailaProducts):
   print("all daila & Kate have the same number of productes")
elif Len(kateProducts)<len(DailaProducts):
   print("kate productes are less than Daila productes")
elif Len(kateProducts)>len(DailaProducts):
   print("kate productes are more than daila productes")
#Print the top selling product from Nestle with sales figures.
for i in kateProducts.items():
   i+=1
   selling=kateProducts[i][1]
   sellingProdList=[]
   sellingProdList.insert(selling)
MaxSalesFig=max(sellingProdList)
MaxProdName=kateProducts[MaxSalesFig]
print(f"the top selling product from Nestle is{MaxProdName} : {MaxSalesFig}")
#Print the top selling product from Unilever with sales figures.
for i in DailaProducts.items():
   i+=1
   selling=DailaProducts[i][1]
   unileversellingProdList=[]
   unileversellingProdList.insert(selling)
unileverMaxSalesFig=max(unileversellingProdList)
unileverMaxProdName=DailaProducts[unileverMaxSalesFig]
print(f"the top selling product from unilever is{unileverMaxProdName} : {unileverMaxSalesFig}")

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("all the cities Unilever & Nestle sell their products in are:")
for i in NestleDec|UnileverDec:
   print(NestleDec|UnileverDec)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("the cities that both Nestle & Unilver sell in common are:")
for i in NestleDec& UnileverDec:
   print(NestleDec& UnileverDec)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("the cities Nestle sells in , but Unilver doens't sell in are:")
for i in NestleDec - UnileverDec:
   print(NestleDec- UnileverDec)







