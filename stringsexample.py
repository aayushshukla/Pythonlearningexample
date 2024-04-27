# immutable - it cant be changed or modified . 
'''
  when we perform any operation in string it will create a new object
  it is index we can access string on basis of index
  it supports indexing similar to list and tuple
  positive indexing starts from 0 and ends at len(string)-1
  negative indexing starts from -1 from the end of string
'''

s='good evening'
s.lower() # lower() convert string in to lowercase
sl=s.lower()
su=s.upper()
st=s.title() # converts string into standard case first word of will be in upper case
sw=s.swapcase() # swap the cases convert upperinto lower and lower into upper
sc=s.capitalize() # converts string first character in to upper case

ind=int(input('enter index to access value'))
#if index is present it will return given character at that index
# if index is not present it will raise error index error 
print(f'character at given index {s[ind]}') 
for ch in s:
    print(ch)

#on basis index
for ind in range(len(s)):
    print(f'ch at [{ind}] = {s[ind]}')

print('length of string',len(s))
print(f'updated string {s}')
print('string in lower case',sl)
print('String in upper case',su)
print('String in standard case',st)
print('String after swap case',sw)
print('String after captilize',sc)