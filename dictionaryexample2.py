dstock={'sbi':550,'mrf':60000,'iocl':180}

# remove a key or key pair from dictionary
#pop(key) it will remove the given and return its value 
# if key is present it will raise error 
stockname=input('enter stock name')

print('Before stock data',dstock)
price =dstock.pop(stockname)
print(f'{stockname} sold at value of {price}')
print('New stock data',dstock)

#popitem() it will remove last key -value pair (item) of dictionary
dstock={'sbi':550,'mrf':60000,'iocl':180}
print('Before stock data',dstock)
item= dstock.popitem()
print(f'last item removed from dictionary {item}')
print('New dictionary after removal of last item',dstock)


dstock2={'hdfc':1100,'ongc':200}
# dictionary1.update(dictionary2) it add all values of dictionary 2 in dictionary1
# merge two dictionaries
print('Old dictionary 1',dstock)
print('old dictionary 2',dstock2)
dstock.update(dstock2)
print('New dictionary 1 after update or merge',dstock)

# clear() remove all elements of dictionary and make empty dictionary

print('Dictionary before clear',dstock)
dstock.clear() 
print('Dictionary after removal of elements or clear',dstock)

#copy() copy one dictionary in to another
d1={}
dstock={'sbi':550,'mrf':60000,'iocl':180}
print('dictionary d1 before copy',d1)
print('Original dictionary',dstock)
d1=dstock.copy()

print('Copied dictionary',d1)
print('Address of original dictionary',id(dstock))
print('Address of  copied dictionary',id(d1))

#fromkeys() Create a new dictionary with keys from iterable and values set to value.
keylist=['c1','c2','c3']
d3={}
d3= d3.fromkeys(keylist,'No Info')
print('Dictionary created from keys',d3)

#create a dictionary name as mydict 
# add following key values in dictionary , emp1 10000 emp2 30000 emp3 50000
# i) show salary of employee 2
# ii) check employee3 is present or not
# iii) remove details of employee3 if present 
# iv ) update the salary of emp1 to 25000
# v) add new employee 4 with salary of 35000

mydict={'emp1':10000,'emp2':30000,'emp3':50000}
print('salary of employee 2',mydict['emp2'])
if mydict.get('emp3')!=None:
    print('Employee is present')
    salary=mydict.pop('emp3')
    print('Employee3 is removed with salary of',salary)
else:
    print('Employee3 is not present')
print('New emplyee list after removal',mydict)
mydict['emp1']=25000
print('New employee updated list ',mydict)
mydict['emp4']=35000
print('New employee list after joining',mydict)


mycollege={'cs':[100,200,300],'me':[50,100,150],'it':[80,240,320]}
branchname=input('enter branch to 3 placement of last 3 yrs')
print(f'{branchname} no of placements = {mycollege[branchname]}')


mycollege={'cs':{2020:100,2021:200,2023:300},'me':{2021:50,2022:100,2023:150}}
# show no of placement from cs branch
print('No placements for cs',mycollege['cs'])
#show no of placement of cs year 2021  dictionary[outdictionarykey][innerkey][innerkey2]
print('No of places for cs in year2021',mycollege['cs'][2021])

branchname=input('enter branch name')
yr=int(input('enter year to check placement'))
if mycollege.get(branchname)!=None:
    if mycollege.get(branchname).get(yr)!=None:
        print('No of placement =',mycollege[branchname][yr])
    else:
        print(f'give {yr} information is not available')
else:
    print(f'{branchname} not found')
    
