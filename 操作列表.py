cities=['paris','london','tokyo','seattle','boston']
for city in cities:
    print(city.title()+" is beautiful!"+"\n")  #首字母大写，空一行

for value in range(1,5):
    print(value)

number=list(range(1,6))
print(number)

even_numbers=list(range(2,11,2))  #开始，停止，步长
print(even_numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

digits=list(range(0,10))
print(sum(digits))

squares=[value for value in range(3,31,3)]
print(squares)

squares=[]
for value in range(1,11):
    square=value**3
    squares.append(square)
print(squares)

squares=[value**3 for value in range(1,11)]
print(squares)


players=['ame','maybe','chalice','fy','xnova']
print(players[-2:])  #倒数2个
for player in players:
    print(player.title())
good_players=players[:]  #复制列表
print (good_players)


good_players.append('yang')
print(good_players)



dimensions=(200,50)
print(dimensions[0])
for dimension in dimensions:
    print(dimension)
