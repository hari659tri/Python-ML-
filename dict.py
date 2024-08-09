list1=[1,2,34,5,6,7]
# list1=list1+list((900,800)) # alternative way
list1.extend([900,800,500])
list1.extend((900,800))
print(list1)