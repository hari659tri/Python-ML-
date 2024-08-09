# import re
# def validpass(password):
#     if(6<=len(password)<=12 and re.search[r'[a-z]',password] and re.search(r'[A-Z]',password) and re.search(r'[0-9]',password) and re.search(r'[$#@]',password)):
#         return True
#     return False


# def checkpassword(password):
#     pasword_list=password.split(',')
#     valid_password=[valid for valid in pasword_list if validpass(valid)]
#     print(valid_password)
#     return ','.join(valid_password)

# password=input("enter comma seperated password")
# print(checkpassword(password))
# import re

# def validpass(password):
#     if (6 <= len(password) <= 12 and
#             re.search(r'[a-z]', password) and
#             re.search(r'[A-Z]', password) and
#             re.search(r'[0-9]', password) and
#             re.search(r'[$#@]', password)):
#         return True
#     return False

# def checkpassword(password):
#     password_list = password.split(',')
#     valid_passwords = [valid for valid in password_list if validpass(valid)]
#     return ','.join(valid_passwords)

# password = input("Enter comma-separated passwords: ")
# print(checkpassword(password))


import re

def validpass(password):
    # Debug statements to check what each condition is evaluating to
    length_ok = 6 <= len(password) <= 12
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[$#@]', password) is not None
    
    print(f"Password: {password}, Length OK: {length_ok}, Has Lower: {has_lower}, Has Upper: {has_upper}, Has Digit: {has_digit}, Has Special: {has_special}")

    if length_ok and has_lower and has_upper and has_digit and has_special:
        return True
    return False

def checkpassword(password):
    password_list = password.split(',')
    valid_passwords = [valid for valid in password_list if validpass(valid)]
    return ','.join(valid_passwords)

password = input("Enter comma-separated passwords: ")
valid_passwords = checkpassword(password)
print(f"Valid passwords: {valid_passwords}")











    