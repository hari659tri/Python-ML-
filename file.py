# f=open('k.txt','r+')
# f.write("doing")
# d=f.read()
# print(d)
# f.close() 
import os
with open("k.txt","r+") as f:
    f.write("thor is tonystark shradha sec fuc ka ho")
    data=f.read()
    print(data)
  
    f.close() #no need to close by your way's'....
    os.remove("k.txt")