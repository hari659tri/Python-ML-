# print("harikesh\r123")
# list=['1','2','3','4']
# str1="-"
# print(str1.join((list)))
# list=[1,2,3,4]
# str='&'.join(map(str,list))
# print(str)
# sgr="aarPWRFR"
# print(sgr.capitalize())
# s="ANDVDFJM34rr4444FDVKMKF"
# st="3344343"
# print(st.isnumeric())

# s="harikesh"
# print(s.center(10,'#'))
# print(s.count('h'))

# l=["abcd","deffg","abcd","abcd"]
# s="0099"
# print(s.isdecimal())

#filter all the number from a given list 
# def filter(list:list)->list:
#     return[word for word in list if word.isdigit()]

# lis=filter(["apple","1234","mango","banana","3456","4560"])
# print(lis)

#filter all the string starting with the vowel:
def filter(list:list)->list:
    # vowel={'a','e','i','o','u','A','E','I','O','U'}
    vowel="aeiouAEIOU"
    return [word for word in list if word.isalpha()]

lis=filter(["apple","Apple","Mango","Ou34t","Ear",'m44534nor',"zbr454","123",'3466'])
print(lis)
