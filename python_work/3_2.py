moto=['honda', 'yamaha', 'suzuki']
print(moto)
moto[0]='ducati'
print(moto) 
moto.append('harley')
print(moto)
moto1 = []
moto1.append('ducati')
moto1.append('honda')
moto1.append('BMW')
print(moto1)
moto.insert(2,'BMW')
print(moto)
del  moto[2]
print(moto)
popped_moto=moto.pop()
print(moto)
print(popped_moto)
last_owned=moto.pop(0)
print(f'The last owned moto is {last_owned.title()}.')
moto.remove('yamaha')
print(moto)
moto=['honda', 'yamaha', 'suzuki']
print(moto)
too_expensive='honda'
moto.remove(too_expensive)
print(moto)
print(f'\nA {too_expensive.title()} is too expensive for me.')
