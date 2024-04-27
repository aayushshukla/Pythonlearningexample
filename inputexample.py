# To take input from user in python we use input()
# syntax input(msg) msg optional 
# input method always return string 

username = input('enter username')
print(f'welcome user = {username}')
age =input("enter age")
print('type of age  ',type(age))
# type conversion converting onee data type into another type 
# int() converts into int , float() to convert string/int into float type
# str() is used to convert into string
iage=int(age) # converting age string in to integer type
print('type of age  ',type(iage))
print(f'{username} age is = {iage*2}')

# converting string into float
expr = float(input('enter user experience'))
print(f'{username} of age {age} having exp of {expr} yr')

amt = int(input("enter amount"))
r = float(input("enter rate of interest"))
t = float(input("enter duration"))
print(f' amount  ={amt} , rate  = {r}% , time is {t}yrs si = {(amt*r*t)/100}')
