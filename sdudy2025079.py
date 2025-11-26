# _*_coding:utf-8_*_
# author: zlg
# create time: 2025/7/19 16:14
# file: sdudy2025079.py
# IDE: PyCharm
# desc: 
# version: v1.0
import re

if __name__ == '__main__':
    print(re.match('www', 'www.runoob.com').group(0))
    line = "Cats are smarter than dogs"
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
    if matchObj:
        print(matchObj)
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(0) : ", matchObj.group(0))
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")

    print(re.search('www', 'www.runoob.com'))  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com'))  # 不在起始位置匹配

    line = "Cats are smarter than dogs"
    searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
        print(searchObj.groups())
    else:
        print("Nothing found!!")

    line = "Cats are smarter than dogs, Tigger are faster than dogs"
    searchObj = re.search(r'(.*?) are (.*?) .*', line, re.M | re.I)
    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
        print(searchObj.groups())
    else:
        print("Nothing found!!")


    # 将匹配的数字乘以 2
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)
    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))

    result = re.findall(r'(\w+)=(\d+)', 'set width20 and height10')
    print(result)