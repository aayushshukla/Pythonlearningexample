#reverse() reverse list
l=[10,20,40,50,60]
l.reverse()
print('reverse list',l)


#copy()
copylist=[]
copylist=l.copy()
print('original list',l)
print('Copied list',copylist)

# extend(iterable)
marvel=['ironman','captain america','hulk','thor']
dc=['spiderman','batman','superman']
print('Marvel old list :',marvel)
print('DC list',dc)
marvel.extend(dc)
print('Marvel dc universer mix list',marvel)

l1=[110,20,40]
l2=[100,300,400]
l1.append(l2)
print('Append',l1)
#l1.extend(100)
#print(l1)

#index(item) it will return the first occurance position of given element
# if element not exists in list it will raise error Value Error

l1=[10,10,20,10,30,10,40,20,40,20,20,10]
element=int(input('enter element to check'))
pos=l1.index(element)
print(f'fist occurance of given {element} = {pos} ')