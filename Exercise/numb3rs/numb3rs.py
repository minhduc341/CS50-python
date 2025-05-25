import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4_pattern = r"^([0-9]?[0-9][0-9]?)\.([0-9]?[0-9][0-9]?)\.([0-9]?[0-9][0-9]?)\.([0-9]?[0-9][0-9]?)$"

    match = re.match(ipv4_pattern, ip)

    if match:
        part1, part2, part3, part4 = map(int, match.groups())

        if (0 <= part1 <= 255) and (0 <= part2 <= 255) and (0 <= part3 <= 255) and (0 <= part4 <= 255):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()