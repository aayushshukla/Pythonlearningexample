'''
   functions- block of statement to perform some specific operation.

   It helps in reusebility of code .
   It makes debugging and maintainance of code easy.

   Function 
     1) Pre defined function or system defined functions example print, input(), max() etc 
     2) User defined functions - defination or body of the function is written by user

    Syntax :
       declaration - for declaration we use def keyword  def functionname(param1,param2...paramN) parametes are optional
       defination  - body of function what work function will do
       calling 

       def functionname(param1,param2...paramN):
           body
    
       
      call : functionname(param1,param2...paramN) parameters are optional
'''
# function without arguments
def add(): # declaration and defination of function
    n1=int(input('enter no 1'))
    n2=int(input('enter no 2'))
    print(f'{n1} + {n2} = {n1+n2}')

print('--before function execution ---')
add() # calling of add function
print('--end function execution ---')



def areaOfTriangle():
    base=float(input('enter base of triangle'))
    height=float(input('enter height of traingle'))
    print(f'area of triangle is  {0.5*base*height}')

areaOfTriangle()

#function with arguments if we have to pass some value inside function from outside a function

def add(x,y):
     print(f'{x} + {y} = {x+y}')

n1=float(input('enter no 1'))
n2=float(input('enter no 2')) 

add(n1,n2)

def createList(list1,totalitem):
    for i in range(totalitem):
        item=input('enter item')
        list1.append(item)
    print('List is',list1)


l1=[]
n=int(input('enter total no items in list'))
createList(l1,n)

# wap to check a year is a leap year or not using function with argument


def checkLeapYear(yr):
    if yr%4==0:
        print(f'{yr} is leap year')
    else:
        print(f'{yr} is not a leap year')

year=int(input('enter year'))
checkLeapYear(year)




