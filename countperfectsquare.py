import math
def count_perfectaquare(N):
    if N<1:
        return 0
    return int(math.sqrt(N))

n=int(input())
print(count_perfectaquare(n))