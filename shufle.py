import random

def shuffle(list:list)->list:
    random.shuffle(list)
    return list


list=[12,34,55,663,22,90]
shuffle(list)
print(list)