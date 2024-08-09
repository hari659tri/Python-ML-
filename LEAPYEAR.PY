def leapyear(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                print("given year is a leap year")
            else:
                print("given year is not a leap year")
        else:
            print("given digit is the leap year")
    else:
        print("it is not a leap year")

y=int(input())
leapyear(y)
