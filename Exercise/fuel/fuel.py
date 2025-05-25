while True:
    try:
        fuel = input('Fraction: ')
        x,y = fuel.split('/')

        z = (int(x) / int(y))*100

        if int(x) > int(y):
            pass
        elif z >= 99:
            print('F')
            break
        elif z <= 1:
            print('E')
            break
        else:
            print(round(z),'%', sep='')
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass