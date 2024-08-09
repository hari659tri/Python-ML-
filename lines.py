lines=[]

while True:
    line=input()
    if len(line)!=0:
        lines.append(line.upper())
    else:
        break
    
for i in lines:
    print(i)
    