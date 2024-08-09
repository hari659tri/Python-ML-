def Convert24(str1):
    
    if str1[-2:]=="AM" and str1[:2]=="12":
        return "00"+str1[2:-2]
    elif str1[-2:]=="AM":
        return str1[:-2]
    elif str1[-2:]=="PM" and str1[:2]=="12":
        return str1[:-2]
    else:
        hours=int(str1[:2])+12
        return str(hours)+str1[2:-3]
   

# Example usage
print(Convert24("08:05:45 PM"))  # Output: 20:05:45
print(Convert24("12:30:30 AM"))  # Output: 00:30:30
print(Convert24("12:45:50 PM"))  # Output: 12:00:00
print(Convert24("01:05:00 PM"))  # Output: 13:00:00
