def change(st:str)->str:
    # a=st[0]
    # b=st[-1] this method give you error because string are immmurtable once created not change 
    # st[0]=b
    # st[-1]=a
    # return st
    return st[-1]+st[1:len(st)-1]+st[0]


s=change("abcd")
print(s)