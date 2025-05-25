from datetime import date
import inflect
import sys

def main():
    dob_input = input("Date of Birth: ")

    age_in_minutes = calculate_age_in_minutes(dob_input)
    print_age_in_words(age_in_minutes)

def calculate_age_in_minutes(dob_input):
    try:
        dob = date.fromisoformat(dob_input)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    age_in_days = (today - dob).days
    age_in_minutes = age_in_days * 24 * 60

    return age_in_minutes

def print_age_in_words(age_in_minutes):
    p = inflect.engine()
    age_words = p.number_to_words(age_in_minutes, andword="", zero="zero")

    print(age_words.capitalize()+" minutes")


if __name__ == "__main__":
    main()