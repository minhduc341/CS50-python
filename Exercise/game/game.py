import random
# input level
while True:
    lvl = input('Level: ')
    try:
        lvl = int(lvl)
        if lvl > 0 :
            n = random.randint(1, lvl)
            # print(n)
            break
        else:
            continue
    except ValueError:
        continue
# input guess number
while True:
    number = input('Guess: ')
    try:
        number = int(number)
        if number > n:
            print('Too large!')
        elif 0 < number < n:
            print('Too small!')
        elif number == n:
            print('Just right!')
            break
    except ValueError:
        continue
