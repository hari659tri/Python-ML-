def lessthan(list,k):
    new_list=[i for i in list if(i<k)]
    return new_list


list=[1,-2,0,5,-3]
k=0
new_list=lessthan(list,k)
print(new_list,type(new_list))

