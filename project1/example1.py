# encoding=utf-8
# 列表
# students=['xiaoming','xiaojuan']
# print students[0]
# students[0]='xiaogou'
# print students[0]
# #元组
# students=（'xiaoming','xiaojuan'）
# print students[0]
# students[0]='xiaogou'
# print students[0]

# 集合
a = set('abcdefmijklmnefcab')
b = set('cdfm')
#交集
x = a&b
#并集
y = a|b
#差集
z = a-b
#去除重复元素
new = set(a)
print(new)
