def plandrome(str1):
    reverse=str1[::-1]   #reversing the string's... 
    if(reverse==str1):
        return True
    else:
        return False
    

if(plandrome("MADAM")):
    print("it is plandrome")
        