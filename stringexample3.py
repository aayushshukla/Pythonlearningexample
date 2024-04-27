'''
  strip(ch) it will remove white space or given character from the extream left and right of the
  string

'''

web='****www.google.com****'
webstrip=web.strip('*')
lweb=web.lstrip('*')
rweb=web.rstrip('*')
print('web address is',webstrip)
print('web address after right strip ',rweb)
print('web address after left strip ',lweb)

d={'c1':100,'c2':200}
key=input('enter key name').strip()
print(f'value for given key {key} = {d[key]}')

st = 'Hello class how are you doing hope you have great week'
l=[]
words=st.split()
print(words)
for word in words:
    if len(word)%2==0:
        print(word)
        l.append(word)
print('even word list',l)
