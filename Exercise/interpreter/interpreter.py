print('Expression:', end=' ')
expression = input()
x, y, z = expression.split(" ")

match y:
    case '+':
        ans = float(int(x) + int(z))
        print(f"{ans:.1f}")
    case '-':
        ans = float(int(x) - int(z))
        print(f"{ans:.1f}")
    case '*':
        ans = float(int(x) * int(z))
        print(f"{ans:.1f}")
    case '/':
        ans = float(int(x) / int(z))
        print(f"{ans:.1f}")