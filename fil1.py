# data=open('demo.txt')
# f=data.read()
# print(f)
# print(type(f))
# data.close()


# # data=open('demo.txt')
# # k=data.readline()
# # print(k)
# #writing to file 
# data=open('demo.txt','w+')
# data.write(" NEW->i am the don\nyou are the also my servant\nchalo phir milte hai byy")
# data.seek(0)
# f=data.read()
# print(f)
# data.close()
# data=open("demo.txt",'a+')
# data.write("harikesh append tripathi")
# data.seek(0)
# f=data.read()
# print(f)
# data.close()

# data=open("demo.txt",'r+')
# data.write("harikesh read tripathi")
# #data.seek(0)
# f=data.read()
# print(f)
# data.close()

# data=open('demo.txt','w')
# L=["hariekesh","mohit",'shubam',"dfj dk kvf d"]
# data.writelines(L) 
# data=open('demo.txt')
# f=data.readlines()
# for line in f:
#     print(line.strip())

# def readline(file):
#     f=open(file)
#     lines=[]
#     while True:
#         line=f.readline()
#         if not line:
#             break
#         lines.append(line.strip())
#     print(lines)
    
# readline("demo.txt")
# def readline(file):
#     var_str=""
#     with open(file,'r') as f:
#         while True:
#             line=f.readline()
#             if not line:
#                 break
#             var_str=var_str+line
#     return var_str

# print(type(readline('demo.txt')))
# print(readline('demo.txt'))

# #wap to read first n line's
# def readline(file,n):
#     with open(file,'r') as f:
#          for i in range(n):
#             line=f.readline()
#             if not line:
#                 break
#             print(line,end="")

# print(readline('demo.txt',2))
# s="haikesh tripati"
# print(type(",".join(s)))
# s="harkesh"
# print(s)
# print(s.strip())

# with open('demo.txt','a+') as f:
#     f.write("sonam kutta mara\n")
#     f.seek(0)
#     print(f.read())

#read the last n lines
# def readlast(n):
#     with open("demo.txt",'r') as f:
#        lines=f.readlines()
#        last_line=lines[-n:]
#        for i in last_line:
#            print(i.strip())
        
# readlast(2)

# print(",".join("tinkuminku"))
# print(",".join("tinkuminku").split())

# s="tinkutripathi"
# print(s.split())

# with open("m.txt","r") as f:
#    str= f.read()
#    new_str=','.join(str)

# with open('m.txt','w') as f:
#     f.write(new_str)
#     print(new_str)

#white space seprated input comes word 
# def printdigit(file,user):
#     with open(file,'w') as f:
#         f.write(user)

# u=input()
# printdigit('m.txt',u)

# def findigit(file):
#     with open(file,'r') as f:
#         data=f.read()
#         list_word=data.split()
#         digi_list=[word for word in list_word if word.isdigit() ]
    
#     for dig in digi_list:
#         print(dig)
        
# findigit('m.txt')

# def countstring(st):
#     letter_count=0
#     digit_count=0
#     for char in st:
#         if char.isalpha():
#             letter_count+=1
#         elif char.isdigit():
#             digit_count+=1
#     return (letter_count,digit_count)

# def addcount(file,letter_count,digit_count):
#     with open(file,'w') as f:
#         f.write(f"number of letter is {letter_count}\nnumber of digit is {digit_count}")
    

# l,m=countstring("python 3.9 is fun! 2024")
# addcount('m.txt',l,m)


# copy one file content to other file 
# f=open('m.txt','r')
# data=f.read()
# n=open('demo.txt','w')
# n.write(data)
# n.close()
# f.close()
# def readlinebyline(file):    
#     arr=[]             
#     with open(file,'r') as f:
#         lines=f.readlines()
      
#         for i in lines:
#             arr.append(i.strip())
        
#         print(arr)

# readlinebyline('m.txt')
       
    
#longest word 
# def longestword(file):
#     with open(file,'r') as f:
#         word=f.read()
#         l_word=word.split()
#         print(l_word)
#         longestword=max(l_word,key=len)
    
#         print(longestword)
        
# longestword('m.txt')
    
# print(max(['hai','ndnsss','dddd'],key=len))
    
# with open('m.txt','r') as f:
#     k=f.read()
#     for line in k:
#         print(line)
#count the number of lines in a text file

# def countlines():
#     with open('m.txt','r') as f:
#         data=f.readlines()
    
#     print(len(data))
    

# countlines()
# def writefile(file,userinput):
#     with open(file,'w') as f:
#           f.writelines(userinput)
#     with open('m.txt','r') as f:
#         lines=f.readlines()
#         for i in lines:
#             if(int(i.strip())%2==0):
#                 with open('even.txt','a') as d:
#                     d.write(i)
#             else:
#                 with open('odd.txt','a') as k:
#                     k.write(i)
        
# userinput=['18\n','19\n','20\n','25\n','33\n']
# writefile('m.txt',userinput)

# f=open('m.txt')
# print(f.closed)
# f.close()
# print(f.closed)
# l=[9,4,5,3,32,2222,22,3,333,33,3,3,3,3]
# print(l.count(3)
# f=open('m.txt','w+')
# f.write('harikesh tripathi\n')
# f.write('sohan tripath\n')
# f.write('mohan kumfjfjar\n')
# f.seek(0)
# d=f.read()
# print(d)
# f.close()
#atmost k occurences 
# def count(list,x,k):
#     a=list.count(x)
#     if a<=k:
#         return True
#     else:
#         return False
    
# print(count([4,4,53,3,5,6,7,88,8,8],3,2))

# f=open('m.txt','w+')
# f.write('hjnfkdms,l.aaaa\njjjjj')
# f.seek(20)
# d=f.read()
# print(d)
# import pandas as pd

# data={
#     'name':['mohan','sohan','rohit','mohit'],
#     'age':[34,45,56,78],
#     'city':['kanpur','banglore','gurugram','noida']
# }
# df=pd.DataFrame(data)
# # print(df)
# # print(df.describe()) 
# print(df.head())
# print(df.columns)
import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)




