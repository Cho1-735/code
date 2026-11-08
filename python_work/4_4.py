players=['charles','martina','michael','florence','eli']
print(players[0:3])#首发包含，尾数不包含
print(players[1:4])
print(players[:])#首发默认从零开始，尾数默认到最后
print(players[-3:])#负数索引从列表末尾开始计数
for player in players[:3]:
    print(player.title())#列表的切片
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]#复制列表
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')#在列表末尾添加元素
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)#区分
