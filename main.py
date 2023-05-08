Nestle_products={
     "KitKat" : "34,456,432 US Dollars",
     "Nescafe" : "14,106,132 US Dollars",
     "Maggi" :  "9,960,312 US Dollars",
     "Nido" : "44,506,003 US Dollars"
}
Unilever_products={
     "Lipton" : "23,456,000 US Dollars",
     "Breyers" : "1,235,891 US Dollars",
     "HellManns": "17,241,412 US Dollars",
     "Marmite" : "11,715,324 US Dollars"

}
#---------------------------------------------
for keys, value in Unilever_products.items():
   print(f"{keys} : {value}")

print("----"*20)

for keys, value in Nestle_products.items():
   print(f"{keys} : {value}")
#--------------------------------------------
if len(Unilever_products)>len(Nestle_products):
   print("Unilever products has more products ")
elif len(Unilever_products)<len(Nestle_products):
   print("Nestle products has more products ")
else:
   print("both of Unilever and Nestle are seem")
#-------------------------------------------------
def change_value_to_number(dicitionary1:dict)->dict:
    new_dict={}
    for key in dicitionary1:
       string_number=dicitionary1[key]
       char_number=""
       for i in string_number:
          if i.isdigit():
             char_number+=i
          if i==" ":
             break
       new_dict.update({key:int(char_number)})

    return new_dict


def display_max(dicitionary1:dict):
   new_dict=change_value_to_number(dicitionary1)
   num=0
   key_name=""
   for key in new_dict:
      if num<new_dict[key]:
         key_name=key
         num=new_dict[key]
   print(f"{key_name} is top selling product , {num} US Dollars")


display_max(Nestle_products)
display_max(Unilever_products)
print()
 #-----------------------------------------------------------------  
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

def sets_operate(frist:set,operator:str,second:set):
   new_set=set()
   if operator=="|":
      new_set=frist |second
   elif operator=="&":
    new_set=frist & second
   elif operator=="^":
      new_set=frist ^ second

   for n in new_set:
      print(n)
   print("--"*40)

sets_operate(Nestle,"|",Unilever)
sets_operate(Nestle,"&",Unilever)
sets_operate(Nestle,"^",Unilever)
   

