dict={}

while True:
    try:
        item = input()
        item = item.upper()

        dict[item] += 1
    except EOFError:
        print('')

        for item in sorted(dict.keys()):
            print(dict[item], item)
            
        break
    except KeyError:
        dict[item] = 1
        pass