for i in range(1,11):
    print(f'value of  {i}')

for i in range(10,110,10):
    print(f'value of {i}')

# print value from 100 to 10 

for i in range(100,0,-10):
     print(f'value of {i}')

name= 'ACODS'
for ch in name:
    print(ch)

#print table of given no using for loop
n=int(input('enter no'))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')

# wap to print all  in between 230 to 560 number that  are multiple of 5 as well as 7
for n in range(230,561):
    if n%5==0 and n%7==0:
        print(f'{n} is multiple 5 as well 7')

# wap to print check no is  prime or not prime
n=int(input('enter no to check prime or not'))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break 
if flag==1:
    print(f'{n} is not a prime no')
else:
    print(f'{n} is a prime no')



# wap to print factorial of a number
# 5!= 5 *4*3*2*1 =120   4!=4*3*2*1 =24   3!=3*2*1 = 6   2=2  1!=1 
n=int(input('enter no to print factorial')) #4
fact =1
for i in range(1,n+1): #1,2,3,4
    print(f'{fact}* {i}= {fact*i}')
    fact=fact*i   # fact=1*1 = 1   fact= 2*1 = 2  fact=2*3 = 6 fact = 6*4=24

print(f'{n}! = {fact}')
n=int(input('enter no to print factorial'))
fact=1
for n in range(n,0,-1):
    print(f'{fact}* {n}= {fact*n}')
    fact=fact *n

print(fact)



   

    

