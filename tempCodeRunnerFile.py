
str1=input("enter a comma seprarted word as a input")
list=str1.split(',')
list.sort()
new_str=",".join(map(str,list))

print(new_str)
