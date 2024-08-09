import numpy as np

# arr = np.array([1,2,3,4,5])
# arr2=np.zeros(10)
# print(arr2)
# arr3=np.arange(10)
# print(arr3)
# s=np.sum(arr)
# print(s)
# n=np.where(arr>=2)
# print(n)

# arr3=np.array([[1,2,3,4,5],[90,50,60,70,800]])


# for i in range(2):
#     for j in range(5): 
#          print(arr3[i,j],end=" " )
#     print()
    
    
# arr4=np.array([1,2,3,4,5,6])
# arr5=arr4.reshape(3,2)
# print(arr5)

# arr=np.array([1,2,3,4,5,6,7,8])
# # arr2=arr.reshape(4,2)
# # print(arr2)
# arr2=np.sqrt(arr)
# print(arr2)
# arr3=np.log(arr)
# print(arr3)

# arr=np.array([[2,4,6],[6,8,10]])
# print(arr)
# print(type(arr))
# print(arr.shape)

# arr=np.array([1,2,3,4,5,6,7])
# s=np.sum(arr)
# avg=np.mean(arr)
# sd=np.std(arr)
# vr=np.var(arr)
# print(s)
# print(avg)
# print(sd)
# print(vr)

#concatenates two array
# arr1=np.array([[1,23,3,4,5,6],[2,3,4,5,0,1],[90,40,60,1,2,3]])
# # arr2=np.array([56,78,80,34,66])
# # con=np.concatenate((arr1,arr2))
# # print(con)

# print(np.transpose(arr1))

#x+y=9 ,x-y=18
# arr1=np.array([1,1])

# solve=np.linalg.solve(np.array([[1,1],[1,-1]]),np.array([9,18]))
# print(solve)
# print(type(solve))
arr=np.array([1,2,3,4,5,6])
# arr2=arr.reshape(3,2)
# arr3=np.transpose(arr2)
# print(arr3)
# md=np.median(arr)
# print(md)

# mt=np.array([[1,2],[3,4],[5,6],[7,8]])
# print(mt)
# arr4=mt.flatten()
# print(arr4)
# idxmin=np.argmin(arr)
# print(idxmin)
# idxmax=np.argmax(arr)
# print(idxmax)

m1=np.array([[4,1],[2,3]])
m2=np.array([[3,4],[5,6]])
# m3=np.dot(m1,m2)
# print(m3) 
# inv=np.linalg.inv(m1)
# print(inv)
# det=np.linalg.det(m1)
# print(det)
# e1,e2=np.linalg.eig(m1)
# print(e1,e2)

co=np.corrcoef(m1)
print(co)
