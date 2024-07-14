list=['1','abc','abc','1','9']
s=0
e=len(list)-1
flag=True
while(s<e):
    if(list[s]!=list[e]):
        print('it is not a plandrome')
        flag=False
        break
    else:
        s=s+1
        e=e-1
        
if(flag==True):  
    print('it is a plandrome')
