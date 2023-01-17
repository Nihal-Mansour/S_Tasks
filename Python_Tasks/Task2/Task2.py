'''
Approach:
first check if the year is divisible by 4 if true, then we will check if it is also divisble by 100 if true
we will move to the last check if the year is divisible also by 400 if true , then this year is a leap year
otherwise it is not a leap year.
'''
def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("Year " + str(year) + " is a leap year")
            else:
                print("Year " + str(year) + " is not a leap year")
        else:
            print("Year " + str(year) + " is not a leap year")
    else:
        print("Year " + str(year) + " is not a leap year")

def main():
    year = input("Enter the year: ")
    is_leap(int(year))

main()

'''
Tests:
2000 => leap
2400 => leap
1800 => not leap
1900 => not leap
2100 => not leap
2200 => not leap
2300 => not leap
2500 => not leap
'''