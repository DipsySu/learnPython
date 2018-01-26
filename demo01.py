
"数据类型"
currentfloat = 100.0
currentInt = 100
currentString = "我是一只小小鸟"
print(currentfloat)
print(currentInt)
print(currentString)

"多变量赋值"
a = b = c = 1
d, e, f = 1, 1.0, "菜鸟教程"

print(e, d, f)
print(a, b, c)

'''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

'''

'''
1. 数字类型包括 int ,float,bool,complex
'''

a, b, c, d = 1, 1.0, True, 4 + 3j

print(type(a), type(b), type(c), type(d))

'''
2. 类型判断,
    type: 不会认为子类是父类的一种类型
    instance : 认为子类时候父类的一种形式
'''

a = 111;
print(isinstance(a, int))

'''
3. 字符串: 

'''

string = "我是一只小小鸟"

print(string[1:])  # 字符串截取
print(string + "-郑钧")  # 字符串拼接
print(string * 10)  # 循环输出字符串

str = r'roo\nn';  # 字符串前面加 r 防自动转义
print(str)
'''
4. list 列表
'''

array = [1,1,2.2,'avfs','sada']
print( array )

'''
5. set
'''
nsset = {1,2,3,4,array}
print(nsset)


a = 1
b = 1
print(a is b)

print(type(a))
print(type(b))
print(id(a))
print(id(b))


a = 300
b = 300
print(a is b)

print(type(a))
print(type(b))

print(id(a))
print(id(b))