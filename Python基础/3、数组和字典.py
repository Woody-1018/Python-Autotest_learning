# 数组
lists = [1, 2, 3, 4, 'SB', 'selenium', 6]
for lists in lists:
    print(lists)
# 字典
# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# key必须唯一，value可以相同
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
dicts = {'username': 'Woody', 'password': '123456'}
print(dicts.keys())
print(dicts.values())
print(dicts.items())
for k, v in dicts.items():
    print('dicts key is %r' % k)
    print('dicts value is %r' % v)

# zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
# 必须和list一起使用，直接使用zip报错
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = list(zip(x, y, z))
print(xyz)


