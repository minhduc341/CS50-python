import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        if (sys.argv[1][-4:]) != '.csv':
            sys.exit('Not a CSV file')
        elif (sys.argv[2][-4:]) != '.csv':
            sys.exit('Not a CSV file')
        else:
            try:
                convert(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit('Could not read '+ sys.argv[1])

def convert(file_1, file_2):
    first = []
    last = []
    house = []
    try:
        with open(file_1, newline='') as csvfile_1:
            reader = csv.DictReader(csvfile_1)
            for row in reader:
                first.append(row['name'].split(',')[1].lstrip())
                last.append(row['name'].split(',')[0])
                house.append(row['house'])
    except FileNotFoundError:
        raise FileNotFoundError

    with open(file_2, 'w', newline='') as csvfile_2:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile_2, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(first)):
            writer.writerow({'first': first[i], 'last': last[i], 'house': house[i]})


    # return table

if __name__ == '__main__':
    main()