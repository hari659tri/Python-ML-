def searchmany(s,x,k):
    count=0
    for i in s:
        if i==x:
            count+=1
          
    if(count==k):
        return True
    else:
        return False
    
print(searchmany([1,2,3,3,3,4,5],3,3))
