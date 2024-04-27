'''
  index(string) -return index/location of given string first occurance if string is not found it will raise error
  rindex(string)-return index/location of given string  last occurance if string is not found it will raise error
  find(string)-return index/location of given string first occurance if string is not found it will return -1
  rfind(string)-return index/location of given string  last occurance if string is not found it will return -1


'''
s='Good evening'
item=input('enter item to search')
floc =s.find(item)
lloc=s.rfind(item)
# fpos=s.index(item)
# lpos=s.rindex(item)

# print(f'first occurance of {item} is at location {fpos}')
# print(f'last occurance of {item} is at location {lpos}')
print(f'first occurance of {item} is at location using find {floc}')
print(f'last occurance of {item} is at location using rfind {lloc}')
if floc!=-1:
    print('item is found')
    print(f'first occurance of {item} is at location {s.index(item)}')
    print(f'last occurance of {item} is at location {s.rindex(item)}')
else:
    print(f'{item} not found in given {s}')
