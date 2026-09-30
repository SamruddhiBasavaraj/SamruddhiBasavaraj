from datetime import date

print("------ Age Calculator ------")

birth_year = int(input("Enter Birth Year : "))
birth_month = int(input("Enter Birth Month (1-12): "))
birth_day = int(input("Enter Birth Day : "))

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print("Today's Date :", today)
print("Your Age is :", age, "years")