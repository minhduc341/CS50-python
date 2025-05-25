import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        z = x + y

        for k in range(3):
            print(x , '+' , y ,'= ', end='')
            ans = int(input())
            if ans == z:
                score += 1
                break
            else:
                print('EEE')
                if k == 2:
                    print(x , '+' , y ,'=', z)
                continue
    print('Score: ',score)

def get_level():
    while True:
        lvl = input('Level: ')
        if lvl in ('1', '2', '3'):
            break

    return int(lvl)

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    else:
        x = random.randint(10 ** (level - 1), 10 ** level - 1)
        y = random.randint(10 ** (level - 1), 10 ** level - 1)

    return x, y

if __name__ == "__main__":
    main()