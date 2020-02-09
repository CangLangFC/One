#1.2.1
print(int(" 45"))
print(str(" 912"))


#1.2.2
x="blue"
y="green"
z=x
print(z)


#1.2.3 组合数据类型
ECN=["austria","iceland","finland","france","germany"]
print(len(ECN[0]))
ECN.append("greece")
print(ECN)


#1.2.4 逻辑操作符
a="1234"
b=None
a is b

# == 等于  ！= 不等于  

# in greece in ECN.

# and, or, not.


#1.2.5 控制流语句
    #if  while

a1=15000
if a1<1000:
    print("small")
elif a1<10000:
    print("medium")
else:
    print("large")

for country in ECN:
    print(country)


#1.2.5.4


#1.2.6 算术操作符
print(12/3)

a=8
a+=8  #相当于a=a+8
print(a)

ECN+=["estonia"]
print(ECN)