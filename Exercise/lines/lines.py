import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        if (sys.argv[1][-3:]) != '.py':
            sys.exit('Not a Python file')
        else:
            try:
                line = lines_of_code(sys.argv[1])
            except FileNotFoundError:
                sys.exit('File does not exist')

    print(line)


def lines_of_code(code):
    try:
        with open(code, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError

    n = len(lines)

    for line in (lines):
        if line.isspace() or (line.lstrip().startswith('#')):
            n = n - 1

    return n


if __name__ == '__main__':
    main()