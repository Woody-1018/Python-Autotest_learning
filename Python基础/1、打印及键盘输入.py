# 打印字符串 %s
name = 'Woody'
print("My name is %s" % name)
# 打印数字类型 %d
age = 28
print("My age is %d" % age)
# 打印未知类型 %r，适用于所有类型
name = 'Woody'
print('My name is %r' % name)
age = 28
print('My age is %r' % age)
# 多个变量打印
print("My Info : %s %d" % (name, age))
print("My Info : %r %r" % (name, age))

# input 键盘输入
String = input("input what you want:")
print("Your input : %s" % String)
