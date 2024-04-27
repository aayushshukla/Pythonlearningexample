n1=float(input('enter no 1'))
n2=float(input('enter no 2'))
print('enter 1 for addition')
print('enter 2 for subs')
print('enter 3 for multi')
print('enter 4  for div')
ch=int(input('enter your choice'))

if ch==1:

    print(f'{n1}+{n2}={n1+n2}')
elif ch==2:
    print(f'{n1}-{n2}={n1-n2}')
elif ch==3:
    print(f'{n1}*{n2}={n1*n2}')
elif ch==4:
    print(f'{n1}/{n2}={n1/n2}')
else:
    print('Invalid operation selected .Please enter valid operation')
