def main():
    print("Greeting:", end = ' ')
    str = input()

    a = value(str)
    print("$"+str(a))

def value(greeting):
    greeting = greeting.lstrip().lower()
    if greeting[0] == 'h':
        if greeting[0:5] == 'hello':
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
