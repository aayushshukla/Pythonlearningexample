s='Monkey.D.Luffy is  king of pirates'
'''
  split(char) it will brake string on basis of given character.
  Default is space.It will return list

'''
wordlist=s.split()
print('words list',wordlist)

email='aayush@gmail.com'
data=email.split('@')
print('Data is',data)
print('User name is',data[0])
print('Domain name is',data[1])

'''
   join(string) on basis on given string 
   it converts list into string 
'''
s1='hello'
joinedstring=','.join(s1)
print('Joined string',joinedstring)

data=['rahul','yahoo.com']
email='@'.join(data)
print('User email is',email)

fn='rahul'
md='kishore'
ln='agarwal'
print('full name',(fn+md+ln))

l=[fn,md,ln]
print('-'.join(l))