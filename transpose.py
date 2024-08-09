m1=[[1,2,4],
    [5,7,9]]

t=[[0,0],
   [0,0],
   [0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
       t[j][i]=m1[i][j]
       


for i in range(len(t)):
    print(t[i])


