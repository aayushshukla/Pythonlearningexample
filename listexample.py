# list - dynamic size size change according to number of items'
# duplicacy - item can repeat itself
# heterogenous - different type of element
# ordered , sequence 
# unsorted
#index 

#create a list

namelist=[]  # empty list
namelist2= list()  # empty list

print('type of namelist',type(namelist))
print('type of namelist2',type(namelist2))

namelist=['ashish','dhanashree','gaganjeet']
print('names are :',namelist)

# access element in list listname[index]
ind = int(input('enter index to get the value'))
name =namelist[ind]
print(f' value at index {ind} = {name}')

#update value at given index listname[index]=newvalue it will update value for given index
# if index not found it will raise error Index Error : list index is out of range

ind = int(input('enter index to  update  the value'))
newvalue=input('enter new name')
print('Names before update :',namelist)
namelist[ind] =newvalue
print('Names after update :',namelist)

# append(item) it adds item at the end of list
print('Names before append :',namelist)
newname=input('enter new name to add in a list')
namelist.append(newname)
print('Names after append :',namelist)

#count(item) it will return no of occurance of given item if item not found it will return 0
empidlist =[101,102,101,105,107,108,101,102,105]
print('total number of in a list',len(empidlist))
empid=int(input('enter id to check its occurance in emplist'))
occur=empidlist.count(empid)
print(f'No of occurance of {empid} in {empidlist} = {occur}')
# insert(index,value) it will add new value at given index
# if index is not present it will add item at the end of list
tvshows=['one piece','naruto','dbz']
print('tv shows list',tvshows)
print('old tv shows list',tvshows)
pos =int(input('enter position to add new tv show'))
showname=input('enter new show name')
tvshows.insert(pos,showname)
print('New tv show list',tvshows)

#pop() it will item from end list  and it will return that item
# if list is empty it will raise error
show=tvshows.pop()
print('Show removed ',show)
print('New show list',tvshows)

for i in range(len(tvshows)):
    show=tvshows.pop()
    print('new show list',tvshows)
print('Tvshow list',tvshows)

#remove(item) it will remove the given item if item not exists it raise error :Value Error
tvshows=['one piece','naruto','dbz']
print('Tvshow list',tvshows)
showname=input('enter show name to remove from tvshows list')
tvshows.remove(showname)
print('Tvshow list after remove',tvshows)








