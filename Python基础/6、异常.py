# http://blog.csdn.net/sinchb/article/details/8392827#
# http://www.runoob.com/python/python-exceptions.html
# 1.Python异常类
# Python是面向对象语言，所以程序抛出的异常也是类。常见的Python异常有以下几个，大家只要大致扫一眼，有个映像，
# 等到编程的时候，相信大家肯定会不只一次跟他们照面（除非你不用Python了）。

# 异常                       描述
# NameError                  尝试访问一个没有申明的变量
# ZeroDivisionError          除数为0
# SyntaxError                语法错误
# IndexError                 索引超出序列范围
# KeyError                   请求一个不存在的字典关键字
# IOError                    输入输出错误（比如你要读的文件不存在）
# AttributeError             尝试访问未知的对象属性
# ValueError                 传给函数的参数类型不正确，比如给int() 函数传入字符串形

# 2.捕获异常
# Python完整的捕获异常的语句有点像：
#
# try:
#     try_suite
# except Exception1,Exception2,...,Argument:
#     exception_suite
# ......   #other exception block
# else:
#     no_exceptions_detected_suite
# finally:
#     always_execute_suite
# 额...是不是很复杂？当然，当我们要捕获异常的时候，并不是必须要按照上面那种格式完全写下来，我们可以丢掉else语句，
# 或者finally语句；甚至不要exception语句，而保留finally语句。额，晕了？好吧，下面，我们就来一一说明啦。

# 2.1.try...except...语句

# try_suite不消我说大家也知道，是我们需要进行捕获异常的代码。而except语句是关键，我们try捕获了代码段try_suite里的异常后，将交给except来处理。
#
# try...except语句最简单的形式如下：

# try:
#     try_suite
# except:
#     exception block
# 上面except子句不跟任何异常和异常参数，所以无论try捕获了任何异常，都将交给except子句的exception
# block来处理。如果我们要处理特定的异常，比如说，我们只想处理除零异常，如果其他异常出现，就让其抛出不做处理，
# 该怎么办呢？这个时候，我们就要给except子句传入异常参数啦！那个ExceptionN就是我们要给except子句的异常类
# （请参考异常类那个表格），表示如果捕获到这类异常，就交给这个except子句来处理。比如：
# try:
#     try_suite
# except Exception:
#     exception block
# 示例
# >>> try:
# ...     res = 2/0
# ... except ZeroDivisionError:
# ...     print "Error:Divisor must not be zero!"
# ...
# Error:Divisor must not be zero!
# 看，我们真的捕获到了ZeroDivisionError异常！那如果我想捕获并处理多个异常怎么办呢？有两种办法，
# 一种是给一个except子句传入多个异常类参数，另外一种是写多个except子句，每个子句都传入你想要处理的异常类参数。
# 甚至，这两种用法可以混搭呢！下面我就来举个例子。
# try:
#     floatnum = float(raw_input("Please input a float:"))
#     intnum = int(floatnum)
#     print
#     100 / intnum
# except ZeroDivisionError:
#     print
#     "Error:you must input a float num which is large or equal then 1!"
# except ValueError:
#     print
#     "Error:you must input a float num!"


#  上面的例子大家一看都懂，就不再解释了。只要大家明白，我们的except可以处理一种异常，多种异常，甚至所有异常就可以了。
#  大家可能注意到了，我们还没解释except子句后面那个Argument是什么东西？别着急，听我一一道来。
# 这个Argument其实是一个异常类的实例（别告诉我你不知到什么是实例），包含了来自异常代码的诊断信息。
# 也就是说，如果你捕获了一个异常，你就可以通过这个异常类的实例来获取更多的关于这个异常的信息。例如：
#
#         [python]
#         view
#         plain
#         copy
#         >> > try:
#             ...
#             1 / 0
#         ... except ZeroDivisionError, reason:
#         ...
#         pass
#         ...
#         >> > type(reason)
#         < type
#         'exceptions.ZeroDivisionError' >
#         >> > print
#         reason
#         integer
#         division or modulo
#         by
#         zero
#         >> > reason
#         ZeroDivisionError('integer division or modulo by zero', )
#         >> > reason.__class__
#         < type
#         'exceptions.ZeroDivisionError' >
#         >> > reason.__class__.__doc__
#         'Second argument to a division or modulo operation was zero.'
#         >> > reason.__class__.__name__
#         'ZeroDivisionError'
#         上面这个例子，我们捕获了除零异常，但是什么都没做。那个reason就是异常类ZeroDivisionError的实例，通过type就可以看出。
#         2.2
#         try ...except...else语句
#         现在我们来说说这个else语句。Python中有很多特殊的else用法，比如用于条件和循环。放到try语句中，其作用其实也差不多：就是当没有检测到异常的时候，则执行else语句。举个例子大家可能更明白些：
#
#         [python]
#         view
#         plain
#         copy
#         >> > import syslog
#         >> > try:
#             ...
#             f = open("/root/test.py")
#         ... except IOError, e:
#         ...
#         syslog.syslog(syslog.LOG_ERR, "%s" % e)
#         ... else:
#         ...
#         syslog.syslog(syslog.LOG_INFO, "no exception caught\n")
#         ...
#         >> > f.close()
#         2.3
#         finally子句
#         finally子句是无论是否检测到异常，都会执行的一段代码。我们可以丢掉except子句和else子句，单独使用try...finally，也可以配合except等使用。
#
#         例如2
#         .2
#         的例子，如果出现其他异常，无法捕获，程序异常退出，那么文件
#         f
#         就没有被正常关闭。这不是我们所希望看到的结果，但是如果我们把f.close语句放到finally语句中，无论是否有异常，都会正常关闭这个文件，岂不是很
#         妙
#         [python]
#         view
#         plain
#         copy
#         >> > import syslog
#         >> > try:
#             ...
#             f = open("/root/test.py")
#         ... except IOError, e:
#         ...
#         syslog.syslog(syslog.LOG_ERR, "%s" % e)
#         ... else:
#         ...
#         syslog.syslog(syslog.LOG_INFO, "no exception caught\n")
#         ... finally:
#         >> > f.close()
#         大家看到了没，我们上面那个例子竟然用到了try,except, else, finally这四个子句！:-)，是不是很有趣？到现在，你就基本上已经学会了如何在Python中捕获常规异常并处理之。
#         3.
#         两个特殊的处理异常的简便方法
#         3.1
#         断言（assert）
#         什么是断言，先看语法：
#
#         [python]
#         view
#         plain
#         copy
#         assert expression[, reason]
#         其中assert是断言的关键字。执行该语句的时候，先判断表达式expression，如果表达式为真，则什么都不做；如果表达式不为真，则抛出异常。reason跟我们之前谈到的异常类的实例一样。不懂？没关系，举例子！最实在！
#
#         [python]
#         view
#         plain
#         copy
#         >> >
#         assert len('love') == len('like')
#                               >> >
#         assert 1 == 1
#                     >> >
#         assert 1 == 2, "1 is not equal 2!"
#         Traceback(most
#         recent
#         call
#         last):
#         File
#         "<stdin>", line
#         1, in < module >
#                 AssertionError: 1 is not equal
#         2!
#         我们可以看到，如果assert后面的表达式为真，则什么都不做，如果不为真，就会抛出AssertionErro异常，而且我们传进去的字符串会作为异常类的实例的具体信息存在。其实，assert异常也可以被try块捕获：
#         [python]
#         view
#         plain
#         copy
#         >> >
#         try:
#             ...
#         assert 1 == 2, "1 is not equal 2!"
#     ... except AssertionError, reason:
#     ...
#     print
#     "%s:%s" % (reason.__class__.__name__, reason)
#     ...
#     AssertionError:1 is not equal
#     2!
#     >> > type(reason)
#     < type
#     'exceptions.AssertionError' >
#
#     3.2.上下文管理（with语句）
#     如果你使用try,except, finally代码仅仅是为了保证共享资源（如文件，数据）的唯一分配，并在任务结束后释放它，那么你就有福了！这个with语句可以让你从try,except, finally中解放出来！语法如下：
#
#     [python]
#     view
#     plain
#     copy
#     with context_expr[as var]:
#         with_suite
#         是不是不明白？很正常，举个例子来！
#         [python]
#         view
#         plain
#         copy
#         >> > with open('/root/test.py') as f:
#             ...
#             for line in f:
#                 ...
#             print
#             line
#         上面这几行代码干了什么？
#
#         （1）打开文件 / root / test.py
#
#         （2）将文件对象赋值给
#         f
#
#         （3）将文件所有行输出
#
#         （4）无论代码中是否出现异常，Python都会为我们关闭这个文件，我们不需要关心这些细节。
#
#         这下，是不是明白了，使用with语句来使用这些共享资源，我们不用担心会因为某种原因而没有释放他。但并不是所有的对象都可以使用with语句，只有支持上下文管理协议（context
#         management
#         protocol）的对象才可以，那哪些对象支持该协议呢？如下表：
#
#         file
#         decimal.Context
#
#         thread.LockType
#
#         threading.Lock
#
#         threading.RLock
#
#         threading.Condition
#
#         threading.Semaphore
#
#         threading.BoundedSemaphore
#
#         至于什么是上下文管理协议，如果你不只关心怎么用with, 以及哪些对象可以使用with，那么我们就不比太关心这个问题：）
#
#         4.
#         抛出异常(
#         raise)
#         如果我们想要在自己编写的程序中主动抛出异常，该怎么办呢？raise语句可以帮助我们达到目的。其基本语法如下：
#
#         [python]
#         view
#         plain
#         copy
#         raise [SomeException[, args[, traceback]]
#         第一个参数，SomeException必须是一个异常类，或异常类的实例
#         第二个参数是传递给SomeException的参数，必须是一个元组。这个参数用来传递关于这个异常的有用信息。
#
#         第三个参数traceback很少用，主要是用来提供一个跟中记录对象（traceback）
#
#         下面我们就来举几个例子。
#
#         [python]
#         view
#         plain
#         copy
#         >> >
#         raise NameError
#         Traceback(most
#         recent
#         call
#         last):
#         File
#         "<stdin>", line
#         1, in < module >
#     NameError
#     >> > raise NameError()  # 异常类的实例
#     Traceback(most
#     recent
#     call
#     last):
#     File
#     "<stdin>", line
#     1, in < module >
# NameError
# >> > raise NameError, ("There is a name error", "in test.py")
# Traceback(most
# recent
# call
# last):
# File
# "<stdin>", line
# 1, in < module >
# >> > raise NameError("There is a name error", "in test.py")  # 注意跟上面一个例子的区别
# Traceback(most
# recent
# call
# last):
# File
# "<stdin>", line
# 1, in < module >
# NameError: ('There is a name error', 'in test.py')
# >> > raise NameError, NameError("There is a name error", "in test.py")  # 注意跟上面一个例子的区别
# Traceback(most
# recent
# call
# last):
# File
# "<stdin>", line
# 1, in < module >
# NameError: ('There is a name error', 'in test.py')
# 其实，我们最常用的还是，只传入第一个参数用来指出异常类型，最多再传入一个元组，用来给出说明信息。如上面第三个例子。
# 5.
# 异常和sys模块
# 另一种获取异常信息的途径是通过sys模块中的exc_info()
# 函数。该函数回返回一个三元组:(异常类，异常类的实例，跟中记录对象)