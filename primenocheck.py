#wap to check a no is a prime no or not using function with argument

def checkPrime(n):
    flag=0
    if n>2:
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if flag==0:
            print(f'{n} is prime no')
        else:
            print(f'{n} is not prime')
    else:
        print('Value should be greater  than or equal 2')


no=int(input('enter no'))
checkPrime(no)
