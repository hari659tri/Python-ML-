# list=[1,1,1,4,2,3,4]
# idx=00,
# list.remove(4)
# while idx<len(list):
#     print(list[idx])
#     idx+=1

list=[1,2,3,4,5,6,7,8,9]
# list.sort(reverse=True)
# print(list)

# l1=list.pop(-3)
# print(l1)

# print("index is :",list.index(3))
# print(list.count(3))
# list.clear()
# print(list)
# print(list[-1:-9:-1])
# print(list[2:8:1])
# list1=[list[i] for i in range(len(list)) if i%2==0]
# print(list1)

# l2=[90,900,500]

# list3=list+l2
# print(list3)

# middle_index=len(list)//2
# # print(list[middle_index:])
# list3=list[middle_index::-1]+list[middle_index+1:]
# print(list3)
# list2=[i%2 for i in list]
# print(list2)
#doing in palce
for i in range(len(list)):
    list[i]=list[i]%2

print(list)