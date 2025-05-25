def main():
    print('Input: ', end = '')
    str = input()

    str = shorten(str)

    print(f'Input: {str}')

def shorten(word):
    for c in word:
        if c in 'AEIOUaeiou':
            word = word.replace(c, '')

    return word


if __name__ == "__main__":
    main()