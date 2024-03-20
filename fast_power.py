import time
import random

def fpow(n,p, counter=0):
    counter +=1
    if p == 0: return 1
    if p % 2 == 0:
        return fpow(n*n, p//2, counter)
    else:
        return n * fpow(n, p-1, counter)

nrange = range(1000)
prange = range(10)
amount = 1000
narr = [random.choice(nrange) for _ in range(amount)]
parr = [random.choice(prange) for _ in range(amount)]

start = time.time()
[print(f'{n: <3} in power {p:^3}: {fpow(n,p)}') for n, p in  zip(narr, parr)]

print("=================")
print(f"Total operations {len(narr)}")
print(f'Execution time {(time.time() - start)*1000:.2f} msec')