# if else 判断，注意分号
a = 5
b = 3
if a >= b:
    print('a > b')
else:
    print('a < b')

# 等于判断 ==
man = 'Wangnima'
if man == 'Wangnima':
    print('%s is SB' % man)
else:
    print('%s is SB as well' % man)

# in,not in 判断
hi = 'hello python'
if 'hello' in hi:
    print('contained')
else:
    print('not contained')

# True,False 布尔类型判断
# 1、有两种值True和
# Flase
#
# 2、布尔类型值得运算
#
# 与运算：只有两个布尔值都为
# True
# 时，计算结果才为
# True。
# True and True  # ==> True
# True and False  # ==> False
# False and True  # ==> False
# False and False  # ==> False
# 或运算：只要有一个布尔值为
# True，计算结果就是
# True。
# True or True  # ==> True
# True or False  # ==> True
# False or True  # ==> True
# False or False  # ==> False
# 非运算：把True变为False，或者把False变为True：
# not True  # ==> False
# not False  # ==> True
# 3、布尔类型还可以与其他数据类型做 and、or和not运算
# 例子：
# a = True
# print
# a and 'a=T' or 'a=F'
# 结果：a = T
# 字符串
# 'a=T'，这是为什么呢？
# Python把0、空字符串
# ''
# 和None看成
# False，其他数值和非空字符串都看成
# True，所以：
# True and 'a=T'
# 计算结果是
# 'a=T'
# 继续计算
# 'a=T' or 'a=F'
# 计算结果还是
# 'a=T'
# and 和 or 运算的一条重要法则：短路计算。

# 多个if循环
score = 90
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# for 循环

i = 'hello world'
for i in i:
    print(i)

animals = ['dog', 'cat', 'pig', 'lion', 'monkey']
for animals in animals:
    print(animals)

# range 函数
# 函数原型：range（start， end， scan):
#
# 参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
#
#          end:计数到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#
#          scan:每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

for i in range(10):
    print(i)
for i in range(0, 10):
    print(i)
for i in range(0, 10, 3):
    print(i)
for i in range(5):
    print(i)
    i += 2
    print(i)
    print('一轮结束')
