#Implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words.
#Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
#And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.


from datetime import date
import re
import sys
import inflect

p=inflect.engine()

def main():
    birth_date=input('Date of birth: ')
    try:
        year, month, day = check_birthday(birth_date)

    except:
        sys.exit('Invalid message')
    date_of_birth=date(int(year), int(month), int(day))
    date_of_today=date.today()
    diff=date_of_today-date_of_birth
    total_minutes=diff.days*24*60
    output=p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + "minutes")



def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day




if __name__ == "__main__":
    main()




