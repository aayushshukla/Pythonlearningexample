amt=10000
wamt=int(input('enter amount to withdraw'))

if wamt<=amt: #outer if
    if wamt>=100: #innr if 1
        if wamt%100==0: #inner if 2
            amt=amt-wamt # amt -= wamt
            print(f'Amount withdraw  = {wamt} ')
            print(f'Balance amount = {amt}')
        else: # else for inner if 2
            print("Amount should multiple of 100,500 or1000")
    else: # else for inner if 1
        print('Amount should be more than or equal to 100 Rs')
else: # else for outer if
    print('Insufficient funds')        

            

