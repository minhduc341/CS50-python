def main():
    while True:
        try:
            fraction = input('Fraction: ')
            percentage =convert(fraction)
            g = gauge(percentage)
            print(g)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(fraction):

    try:
        x,y = fraction.split('/')
        z = (int(x) / int(y))*100
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

    if z > 100:
        raise ValueError
    else:
        return round(z)

def gauge(percentage):

    if percentage >= 99:
        return 'F'
    if percentage <= 1:
        return 'E'
    else:
        percentage = str(percentage)
        return percentage+'%'


if __name__ == "__main__":
    main()