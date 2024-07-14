# open('practice.txt','r') as f
def even():
 with open('t.txt','r') as f:
    data=f.read()
    print(type(data))
    new_d= data.split(",")
    print(new_d)
    print(type(new_d))
    i=0
    cnt=0
    for val in new_d:
        if(int(val)%2==0):
            cnt+=1 
       
    
    return cnt

a=even()
print("even is",a)
s='ht'
print(s)
s='ukt'
print(s)

s='1 2 3 4 5'
print(type(s))
k=s.split()
print(k)
print(type(k[0]))

