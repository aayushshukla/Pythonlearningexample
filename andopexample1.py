n=int(input('enter no to check it is multiple of 10 as well as 2'))

if n%10==0 and n%2==0:
    print(f'{n} is multiple of both 2 and 10')
else:
    print(f'{n} is not multiple of both 2 and 10')


amt=10000
wamt=int(input('enter amount to withdraw'))

if wamt<=amt and wamt>=100 and wamt%100==0:
    amt-=wamt
    print(f'Amount withdraw  = {wamt} ')
    print(f'Balance amount = {amt}')
else:
    print('Check the amount entered, it is insufficient or invalid amt entered')

