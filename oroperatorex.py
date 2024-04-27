print('Enter PAN for pancard')
print('Enter ADHAAR for adhaar card')
idtype=input('enter id type it is pan or adhaar ')
if idtype=='PAN' or idtype=='ADHAAR':
    idno=input('enter id proof no')
    print(f'Welcome : {idtype} no {idno}')
else:
    print(f'Invalid idtype please use adhaar or pancard for idproof')