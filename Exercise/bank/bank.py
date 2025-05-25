print("Greeting:", end = ' ')
str = input()

ans = str.lstrip().lower()

if ans[0] == 'h':
    if ans[0:5] == 'hello':
        print('$0')
    else:
        print('$20')
else:
    print('$100')