#Implement a program that prompts the user for a date, anno Domini, in month-day-year order,
#formatted like 9/8/1636 or September 8, 1636. Then output that same date in YYYY-MM-DD format.
#If the user’s input is not a valid date in either format, prompt the user again.
#Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

date=input('Date: ')
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        month, day, year = date.split("/")
        if (int(month>=1) and int(month<=12)) and (int(day>=1) and int(day<=12)):
            break

    except:
        try:
            old_month,old_day,old_year=date.split(" ")
            for i in range(len(months)): #we want to know the position of the element in the date list
                if old_month == months[i]:
                    month=i+1
            day=old_day.replace(",", "")  #First you put what you want to replace, then for what you want to replace it
            if (int(month>=1) and int(month<=12)) and (int(day>=1) and int(day<=12)):
                break
        except:
            print()
            break


#If mont or day is less than 10, print a 0 before:
print(f"{year}-{int(month):02}-{int(day):02}")


