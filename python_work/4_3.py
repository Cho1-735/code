for value in range(1,5,1):#第二位数表示结束值（不包含），第一位数表示起始值（包含），第三位数表示步长
    print(value)
numbers=list(range(1,10,2))
print(numbers)
squares=[]
for value in range(1,11):
    #square=value**2
    #squares.append(square)
    squares.append(value**2)#等价line7+8，square作为临时变量
print(squares)
digits=[1,2,3,4,5]
print(min(digits))
print(max(digits))
print(sum(digits))  
squares=[value**2 for value in range(1,11)]
print(squares)#列表推导式