dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = float(0)

while True:
    try:
        order = input('Item: ')
        order = order.lower().title()

        total += dict[order]
        print('$',"%.2f" % total, sep='')

    except EOFError:
        break
    except KeyError:
        pass