year = int(input('Enter a year to check leap or not: '))
'''if year % 400 == 0:
    print('It is a leap year')
elif year % 100 == 0:
    print('It is not a leap year')
elif year % 4 == 0:
    print('It is a leap year')
else:
    print('It is not a leap year')'''
if (year%400==0 and year%100!=0)or(year%4==0):
    print('it is a leap year')
else:
    print('it is not a leap year')
