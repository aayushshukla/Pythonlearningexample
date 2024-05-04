''' types of arguments

    i) positional arguments
    ii) key word arguments or named arguments
    iii) default arguments
    iv) arbitarty value arguments
    v) arbitary keyword arguments


'''

# positional arguments
def fn(x,y):
    print(f'value of x = {x} and value of y = {y}')
 # fn(100) fn() missing 1 required positional argument: 'y'
fn(10,20)

# keyword arguments or named arguments
def fn(x,y):
    print(f'value of x = {x} and value of y = {y}')
# keyword args use during calling of function
fn(y=10,x=20)
#fn(y=20,30) Positional argument cannot appear after keyword arguments

# default arguments are defined during declaration of function
def fn(fn,mn='',ln='doe'):
    print(f'first name = {fn} ,middle name = {mn} and last name  = {ln}')

fn('John')
fn('Aayush',ln='Shukla')
fn('Monkey','D.','Luffy')


# arbitary value argument  -- if u are not sure regarding no of arguemts that user can pass 
# we can user arbitary value arguments
# syntax = *argumentname  , arguments will be stored in form of tuple

def fn(*v):
    print('--------------------------')
    print(v)
    for arg in v:
        print(arg)
    print('============================')

fn(100,200)
fn('a','b','c','d')
fn(1,2,4,5,6,7,8,9,10)

# if we are passing multiple arguments positional and arbitary value argument must be last 
def fn(firstarg,*v): 
    print('--------------------------')
    print('first argment \t ',firstarg)
    for arg in v:
        print(arg)
    print('============================')

fn(100,200)
fn('a','b','c','d')
fn(1,2,4,5,6,7,8,9,10)

# arbitary keyword arguments use if not sure how many named argument user will pass
# syntax = **argumentname arguments will stored in form of dictionary

def fn(**kw):
    print('-----------------------')
    print(kw)
    print('=====================')


fn(x=10,y=20)
fn(un='aayush',md='',ln='shukla')
fn(l=100,m=200,n=500,z=900)

# arbitary value arguement and keyword argument first write arbitary value arg than kw args
def fn(*v,**kw):
    print(v)
    print('-----------------------')
    print(kw)
    print('=====================')


fn(100,200,300,x=10,y=20)
fn(un='aayush',md='',ln='shukla')
fn(1,2,l=100,m=200,n=500,z=900)

