cars=['bmw','audi','tesla','honda']
print(cars)
cars.sort()#永久改变顺序
print(cars)
cars.sort(reverse=True)#永久改变顺序
print(cars)
cars=['bmw','audi','tesla','honda']
print(f"Here is the original list:\n{cars}")
print(f"\nHere is the sorted list:\n{sorted(cars)}")
print(f"\nHere is the original list again:\n{cars}")
print(cars)
cars.reverse()#不是按字母顺序排列，而是将列表中的元素顺序反转
print(cars)
cars.reverse()#改变为原来顺序
print(cars)
print(len(cars))