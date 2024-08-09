def check(list):
   len1=len(list)
   if(len1==0):
       return True
   elif len1==1:
       if list[0]%2==0:
           return True
       return False
   elif list[0]%2==0:
       for i in range(len(list)-1):
           if(list[i]%2==list[i+1]%2):
               return False
       else:
           return True
                         
   else:
       return False
         

print(check([]))
print(check([90]))
print(check([10,20]))
print(check([20,27,80]))
print(check([8,9,10,11]))
print(check([10,8,8]))

           
            
       
        