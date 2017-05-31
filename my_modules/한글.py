from 한글 import *

# Replace 'print()'
def 출력(string):
    return print(string)

# Replace 'input()'
def 받아라():
    temp = input()
    return temp

# Replace 'int()'
def 정수(string):
    return int(string)

# Replace 'float()'
def 실수(string):
    return float(string)


# Replace 'range()'
def 범위(*a):
    if ((len(a) == 0) or (len(a) >= 4)):
        return ValueError
    if len(a) == 1:
        return range(a[0])
    if len(a) == 2:
        return range(a[0], a[1])
    if len(a) == 3:
        return range(a[0], a[1], a[2])


# Replace 'import'
def 가져와라(module):
    import module

# Replace 'for'
def 순차반복():
    return 0

# Replace 'while'
def 조건반복():
    return 0


# Replace 'if'
def 만약():
    return 0
