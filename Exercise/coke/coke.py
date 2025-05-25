def main():
    amount_due = 50

    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        print('Insert Coin: ', end = '')
        insert = int(input())
        if insert == 25 or insert == 10 or insert ==5:
            amount_due = amount_due - insert
        else:
            insert = 0
    amount_due = abs(amount_due)
    print(f'Change Owed: {amount_due}')


main()