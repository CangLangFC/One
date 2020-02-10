ECN=['austria','iceland','finland','france','germany']
print(ECN[-1].title())   #倒数第一个
ECN[0]='croatia'
print(ECN)
ECN.append('austria')    #在后边添加
print(ECN)
ECN.insert(1,'estonia')  #指定位置添加
print(ECN)
del ECN[0]               #删除指定
print(ECN)
ECN1=ECN.pop()           #弹出最后一个（栈顶）
print(ECN)
print(ECN1)
ECN.remove('iceland')
print(ECN)



