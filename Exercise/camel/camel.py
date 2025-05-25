print('camelCase: ', end = '')
str = input()

for c in str:
    if c.isupper():
        str = str.replace(c, '_' + c.swapcase())


print('snake_case: ', end = '')
print(str)