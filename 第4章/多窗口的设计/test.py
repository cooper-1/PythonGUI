# -*-coding:  UTF-8
# @Time    :  2021/8/17 17:35
# @Author  :  Cooper
# @FileName:  test.py
# @Software:  PyCharm
import re
s="大家好，我是一个程序员小白。I 'm so glad to introduce myself, and I’m 18 years old.   Today is 2020/01/01. It is a wonderful DAY! @HHHHello,,,#111ComeHere222...66？AA？zz？——http.//welcome.cn"
print(re.sub(r'http[:.]+\S+', '', s))
print(re.sub(r'http:\S+', '', s))
print(re.sub(r'http[:]\S+', '', s))#使用方括号 [ ] 包含一系列字符，能够匹配其中任意一个字符。\S 匹配所有非空白字符（"\s") + 可匹配各个空白字符）表达式至少出现1次，相当于 {1,}
# "大家好，我是一个程序员小白。I 'm so glad to introduce myself, and I’m 18 years old.   Today is 2020/01/01. It is a wonderful DAY! @HHHHello,,,#111ComeHere222...66？AA？zz？——"

