# -*- coding=utf-8 -*-
# 给变量 x 赋值
x = "There are %d types of people." % 10
# 给变量 binary 赋值
binary = "binary"
# 给变量 do_not 赋值
do_not = "dont't"
# 给变量 y 赋值, 并格式化字符串
y = "Those who know %s and those who %s." % (binary, do_not)

# 输出变量 x
print x
# 输出变量 y
print y

# 输出字符串格式化的 r
print "I said: %r." % x
# 输出字符串格式化的 s
print "I also said: '%s'." % y


# 给变量 hilarious 赋值 False
hilarious = False
# 字符串包含格式化的
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印字符串
print joke_evaluation % hilarious

# 给 w 赋值
w = "This is the left side of..."
# 给 e 赋值
e = "a string with a right side."

# 打印变量 w 和 e 的拼接
print w + e
