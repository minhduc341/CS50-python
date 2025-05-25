import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_period = r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$'
    match = re.match(time_period, s)

    # print(match.groups())
    # convert
    if match:
        start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()
        if start_meridiem == "AM":
            start_hour = int(start_hour) % 12
        else:
            start_hour = (int(start_hour) % 12) + 12

        if end_meridiem == "AM":
            end_hour = int(end_hour) % 12
        else:
            end_hour = (int(end_hour) % 12) + 12

        # check valid time
        if (start_minute != None) and (end_minute != None):
            if 0 <= int(start_hour) <= 23 and 0 <= int(end_hour) <= 23 and 0 <= int(start_minute) <= 59 and 0 <= int(end_minute) <= 59:
                return f"{start_hour:02d}:{start_minute} to {end_hour:02d}:{end_minute}"
            else:
                raise ValueError("Invalid time")
        elif (start_minute == None) and (end_minute == None):
            return f"{start_hour:02d}:00 to {end_hour:02d}:00"
        else:
            raise ValueError("Invalid time")
    else:
        raise ValueError("Invalid format")

if __name__ == "__main__":
    main()