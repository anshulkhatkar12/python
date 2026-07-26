#getting i^2 when i<n
n = int(input())
for i in range(n):
    print(i*i)

#year is leap year or not
def is_leap(year):
    leap=False
    if year%4==0:
        leap=True
        if year %100==0:
            leap=False
            if year%400==0:
                leap=True
    return leap
year = int(input("year:"))
print(is_leap(year))