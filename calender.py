import calender
def print_cal(year):
    cal = calender.textcal()
    for month in range(1,13):
        print(cal.formatmonth(year,month))

if __name__ == "__main__":
    try:
        year=int(input("Enter the year: "))
        print_cal(year)
    except ValueError:
        print("Please enter a valid year.")
