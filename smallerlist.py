def ret_smaller(list):
    if len(list)==0:
        return []
    smaller_list=list[0]
    for i in range(1,len(list)):
        if(len(list[i])>len(smaller_list)):
            smaller_list=list[i]
    return smaller_list

print(ret_smaller([[1,2,3],[3,4],[40,90,900,700,609],[90],[80]]))
            
            