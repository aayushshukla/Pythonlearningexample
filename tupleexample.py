# create tuple 
t=() # empty tuple
t1=tuple() # empty tuple
print('type of t and t1 ',type(t) ,'\t',type(t1))

t1=(10,20,30,30,10,20,40,30)
# access data from tuple  tuplename[index] it will return value for given index
# if index does not exists it will raise error index error
index =int(input('enter index to access value'))
value =t1[index]
print(f'value for index {index} = {value}')
# accessing tuples value on basis of index
for ind in range(len(t1)):
    print(f't1[{ind}] = {t1[ind]}')

# iteration over tuple value
for item in t1:
    print(item)

# t1[1]=100 TypeError: 'tuple' object does not support item assignment

#count(element) no of occurance of item , if item is not found it will return 0
item=int(input('enter item to search'))
occ=t1.count(item)
if occ==0:
    print(f'{item} not found in given tuple {t1} ')
else:
    print(f'{item} found .No of occurance of {item} = {occ}')

#index(element) it will return the first location occurance of given item 
# if item is not present it will raise error

item=int(input('enter item find its position  '))
pos = t1.index(item)
print(f'{item} first occurance found at index {pos}')


#packing and unpacking 
t2=100,200,300,40,50
print('value of t2 =',t2)

#unpacking 
x,y,z,l,m=t2
print(f'value of x , y ,z  = {x} {y} {z}')
print(f'value of l,m = {l} {m} ')


# wap to create user defined tuple 
# no of item  , items 
l=[]
n=int(input('enter no of items'))
for i in range(n):
    item=input('enter items')
    l.append(item)

t=tuple(l)
print('tuple is =',t)
# swap two number without using third variable 
n1=100
n2=200
n1,n2 = n2,n1
print('value after swap',n1,n2)
# square of all elements of tuple 
t3=(10,20,40)
for item in t3:
    print(f'square of {item} ={item**2}')
