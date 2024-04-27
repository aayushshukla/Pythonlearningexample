i=1  # intialiase 
#while condition : body
while i <=10:
    print('value of i :',i)  # 1,2  ,3....10
    i=i+1   # i =1+1 =2  i=2+1=3 i=10+1=11

# wap to print square of all no between 25 to 50
    
n=25

while n<=50:
    print(f'{n}**2 = {n**2}')
    n=n+1

# wap to print number from 100 t0 45
n=100
while n>=45:
    print('value of n is ',n)
    n=n-1
# wap to print cube of all no in range 10 to 15    
n=10
while n<=15:
    print(f'cube of {n} = {n**3} ')
    n=n+1
# wap to print table of a given no 
n=int(input('enter a number'))
i=1
while i <=10:
    print(f'{n} * {i} = {n*i}')    
    i=i+1
#wap to print all the even numbers in range of 10 to 100
n=10
print('----even nos----')
while n<=100:
    if n%2==0:
        print(f'{n}',end=' ')
    n=n+1