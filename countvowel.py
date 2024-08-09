# def count(st:str)->int:
#     cnt=0
#     vowel="aeiouAEIOU"
#     for s in st:
#         if s in vowel:
#             cnt+=1
  
#     return cnt

# a=count("appleAPPiou")
# print(a)
    
#check plandrome
def plandrom(str):
    reverse=str[::-1]
    return str==reverse

ass=plandrom("mamamamam")
if(ass):
    print("yes it is plandrome")
else:
    print("it is not a plandrome")
 
    