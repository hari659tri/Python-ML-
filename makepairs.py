
# s=() # empty tuple 
# print(type(s))
def makepairs(list1,list2):
    len1=len(list1)
    len2=len(list2)
    if(len1==len2):
      new_list=[(list1[i],list2[i]) for i in range(len1)]
      return new_list
    else:
        return []
    
    
list= makepairs([1,2,3],[1,2,3])
print(list)