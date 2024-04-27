# non index , non sequencial 
# key:value , pair data, dynamic size 
# keys are unique , there will be no duplicacy of key
 # key are immutable 
#  value can repeat 

#create 
d1 = {}  # empty dictionary
d2=dict() # empty dictionary
print('type of d1 and d2',type(d1),'\t',type(d2))
# dictionaryname={key1:v,key2:v2..}
dmenu = {'momos':60,'paneer roll':100,'dosa':90}

#get data  =  1) dictionaryname[key] if key is present it return value for given key
# if is not present than it will raise error  key error
#item=input('enter dish name')
# if dmenu.get(item)!=None:
#     price =dmenu[item]
#     print(f'{item} ={price} inr')
# else:
#     print('Dish not available at this time')

# #get(key) it will return value of given key if key is not present it will return none
# price2=dmenu.get(item)
# print(f'{item} ={price2} ')

# #update a  key or add key value pair  dictionaryname[key]=value
# # if key is present it will update value for given key
# # if key is not present it will add new key value pair at the end of dictionary
# dishname=input('enter dishname')
# value =int(input('enter new value'))
# print('Old menu',dmenu)
# dmenu[dishname]=value
# print('New menu',dmenu)
#keys() returns keys of dictionary
dmenu = {'momos':60,'paneer roll':100,'dosa':90}
dishesname=dmenu.keys()
print(dishesname)
for key in dmenu.keys():
    print(key)

#values() - returns all the values of dictionary
prices =dmenu.values()
print("dishes prices ",prices)

for price in dmenu.values():
    print(price)

#items() - returns all (key,value)  of dictionary

menu =dmenu.items()
print(menu)

for key,value in dmenu.items():
    print(f'{key} = {value}')


