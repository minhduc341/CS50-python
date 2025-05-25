list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ')
        month, day, year = date.split('/')

        month = int(month)
        day = int(day)
        year = int(year)

        if day > 31 or month > 12:
            pass
        else:
            print(year, f"{month:02}", f"{day:02}", sep = '-')
            break
    except ValueError:
        try:
            month, d_y = date.split(maxsplit=1)

            month = list.index(month) + 1
            day, year = d_y.split(',')
            day = int(day)
            year = int(year)

            if day > 31 or month > 12:
                pass
            else:
                print(year, f"{month:02}", f"{day:02}", sep = '-')
                break
        except ValueError:
            pass

