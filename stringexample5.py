username=input('enter first name')
password=input('enter password')

if username.isalpha():
    print('Valid user name')
else:
    print('Invalid username only alphabets allowed')


if password.isalnum() and len(password)>=8 and len(password)<=16:
    print('Password is valid')
else:
    print('Invalid password')


''' escape character
   /n - new line
   /t   tab 
   /r 

'''
para ='Hello class \n how are you doing ? \n  Hope you guys have great weekend \t enjoy'
print(para)
np=0 # variable for calculating number of non printable character
for word in para:
    if word.isprintable():
        pass 
    else:
        np+=1
print('No of words in para',len(para.split()))
print('No of non printable character in para',np)

sp=0
for word in para:
    if word.isspace():
        sp+=1
    
print("Total spaces =",sp)

s1='Hello'
replacestring=s1.replace('l','*')

print('replaced string',replacestring)

'''
   Write a Python program to find the first appearance of the substrings 'not' and 'poor'
   example='The lyrics are not that poor' 
   example2='The lyrics are not poor'
   in a given string. If 'not' follows 'poor', 
   replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

'''
str=input('enter string')
pnot=str.find('not')
ppoor=str.find('poor')

if pnot!=-1 and ppoor!=-1:
    newstr=str.replace('not poor','good')
    print('new string',newstr)
else:
    print('Not and poor not present')

'''
  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
  If the given string already ends with 'ing', add 'ly' instead.
  If the string length of the given string is less than 3, leave it unchanged.
'''

str='song.mp4'
if str.endswith('.mp4'):
    print('Playing video',str)
else:
    print('Only .mp4 format supported')

if str.startswith('a'):
    print('string is  starting with a')
else:
    print('String is not starting with a')

