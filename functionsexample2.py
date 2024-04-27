# function with return

def add():
    # n1, n2 , res are local variable 
    #  local variable : variable that have scope only inside a function or a block
    n1=int(input('enter no1'))
    n2=int(input('enter no2'))
    res = n1+n2
    # whenever we have have to return a value we have use return keyword
    return res # it is last statement of function 
    print('--------------------') # unreachable code 

sum =add()
print('sum is ',sum)

# function with argument and with return type
def checkEven(n):
    if n%2==0:
        return 'Even number'
    else:
        return 'Odd no'
    
n=int(input('enter no'))
res= checkEven(n)
print(f'{n}  {res}')

# wap to create function  take first name , last name as input and return full name


def createUserName(fn,ln):
    return fn+ln

firstname =input('enter firstname')
lastname =input('enter last name')
username=createUserName(firstname,lastname)
print('Welcome user ',username)
