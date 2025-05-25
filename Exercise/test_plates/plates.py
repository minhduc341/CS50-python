def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    else:
        for c in s[0:2]:
            if c.isdecimal():
                return False

        for c in s:
            if c in '.?':
                return False
            if c.isspace():
                return False

        ind = len(s) + 1
        for c in s[2:]:
            if c.isdecimal():
                ind = s.index(c)
                break

        if ind != len(s) + 1:
            if s[ind] == '0':
                return False
            for c in s[ind+1:]:
                if c.isalpha():
                    return False
            return True
        else:
            return True

if __name__ == "__main__":
    main()