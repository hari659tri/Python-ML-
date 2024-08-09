# from math import sqrt

# def perfect(number):
#     sqroot=int(sqrt(number))
#     if(sqroot**2==number):
#         return number
#     else:
#         return -1
    
    
# n=int(input())
# num=perfect(n)
# print(num)

# import datetime

# now = datetime.datetime.now()
# print(now)  # Output: Current date and time

# today = datetime.date.today()
# print(today)  # Output: Current date

# new_year = datetime.datetime(2024, 1, 1)
# print(new_year)  # Output: 2024-01-01 00:00:00

# delta = datetime.timedelta(days=10)
# print(today + delta)  # Output: Date 10 days from today

# date_str = '2024-08-04'
# date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
# print(date_obj)  # Output: 2024-08-04 00:00:00

# formatted_date = date_obj.strftime('%B %d, %Y')
# print(formatted_date)  # Output: August 04, 2024
# import calendar

# # print(calendar.calendar(2026))


# #check year is leap year or not
# def isLeap(year:int)->bool:
#     return calendar.isleap(year)
# year=int(input())
# if isLeap(year):
#     print("yes")
# else:
#     print("no")

# s="harikesh,tripathi,is,don,of,the,india"
# text=s.split(",")
# print(text)
# print("- ,k".join(map(str,(text))))

# str1=input("enter a comma seprarted word as a input")
# list=str1.split(',')
# list.sort()
# new_str=",".join(map(str,list))

# print(new_str)

# import itertools
# def permtationstring(st):
#     s=list(itertools.permutations(st))
#     return[''.join(word)for word in s]
    
# str1="abc"
# prem_str=permtationstring(str1)
# print(prem_str)

# a,b,c=1,2,3
# print(a,b,c)

a=['12','hello']
# a[0]*=3
# print(type(a[0]))

a[0][0]="900"
print(a)