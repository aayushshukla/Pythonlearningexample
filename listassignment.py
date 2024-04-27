
'''l=[]
n=int(input('enter number of item in a list'))

for i in range(n):
    item=input('enter value')
    l.append(item)

print(l)

ctemp=[]
n=int(input('enter no of cities to record data'))
for i in range(n):
    ctemp.append(float(input('enter temp in degree')))
print('temperature in degree')
print(ctemp)

ftemp=[]
for temp in ctemp:
    faren= ((temp)*9/5)+32
    ftemp.append(faren)

print(ftemp)

l=[10,20,30,45,54,33,31,65,13]
for item in l:
    if item%2==0:
        print('even :', item)


'''
# l =[10,11,43,24,56,67] sum of all the elements of list
        
l =[10,11,43,24,56,67]
total=0
for index in range(0,len(l)):
    print(f'{index} = {l[index]}')
    total=total+l[index]  #  total=0+10 = 10  , total=10+11=21 , total=21+43=64 , total=64+56=120
    # total=120+67=187

print('sum is =',total)

# l =[10,11,12,14,67,56,78,10,10]  enter element to search = ?
# if element present show found otherwise show not found 
# no of occurance of given element 
'''l =[10,11,12,14,67,56,78,10,10]
ele=int(input('enter element  to search'))
if ele in l:
    occ=l.count(ele)
    print(f'{ele} no of occurances ={occ}')
else:
    print(f'{ele} is not found ')

occ = l.count(ele)
if occ !=0:
    print(f'{ele} is found and no of occ is {occ}' )
else:
    print(f'{ele} is not found ')
'''
l =[10,11,12,14,67,56,78,10,10]
ele=int(input('enter element  to search'))
c=0
for i in range(0,len(l)):
    if ele==l[i]:
        c=c+1

if c!=0:
    print(f'{ele} is found and no of occurances = {c}')
else:
    print(f'{ele} is not found')

# playermatches=[10,20,40,50]
# playerruns=[450,400,1600,2500]
# playeravg=[45,20,40,50]
    
playermatches=[10,20,40,50]
playerruns=[450,400,1600,2500]
playeravg=[]
for i in range(0,len(playermatches)):
    avg=playerruns[i]/playermatches[i]
    playeravg.append(avg)
print('Player matches =',playermatches)
print('Player runs =',playerruns)
print('Player avg =',playeravg)