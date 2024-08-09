# def sum(*args):
#     s=0
#     for i in args: # internally work as a list...
#         s=s+i
#     return s

# print(sum(10))
# print(sum(10,20,30))
# print(sum(10,20,30,40))

def s(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        

s(rohan=23,mohan=45)