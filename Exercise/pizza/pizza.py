import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        if (sys.argv[1][-4:]) != '.csv':
            sys.exit('Not a CSV file')
        else:
            try:
                table = format(sys.argv[1])
            except FileNotFoundError:
                sys.exit('File does not exist')

    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))

def format(csv_file):
    table = []
    try:
        with open(csv_file) as file:
            for line in file:
                table.append(line.rstrip().split(","))
    except FileNotFoundError:
        raise FileNotFoundError

    return table

if __name__ == '__main__':
    main()