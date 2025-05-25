def main():
    print('What time is it?', end = ' ')
    time = input()
    time = convert(time)

    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(":")
    hour = float(hours)
    min = float(minutes)

    return hour + (min / 60)


if __name__ == "__main__":
    main()