# # print 1 to n
# def show(n):
#     #base case......
#     if(n==0):
#         return 
#     print(n,end=" ")
#     show(n-1)
    
    

# show(5)
#print list element
list=['harikesh','ravi',1,2,3,4,5,6]
def show(list,idx):
    if(idx==len(list)):
        return 
    print(list[idx],end=" ")
    show(list,idx+1)
    
    
    
    
show(list,0)
    