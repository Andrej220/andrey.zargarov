import time

# in case of a real big number
import sys
sys.set_int_max_str_digits(1000000)

# Calculating n-th Fibonacci number
# it tates 2,5 sec to caluculate 2_000_000th fibonacci number
# https://web.archive.org/web/20220614001843/https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4

# approximation, 
def fib_approximation(n):
    sqr = 5**0.5
    a = (1 + sqr)/2
    b = (1 - sqr)/2
    return  ((pow(a,n) - b**n)/sqr)//1

# stright forward algoritm
def fib_linear(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# exponential algoritm
def fib_exp(n):
    k = 1
    if n < 0: k = int((-1)**(n+1))
    return k * fib_iter(1, 0, 0, 1, abs(n))

def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    elif count % 2 == 0:
        return fib_iter(a, b, p*p + q*q, 2*p*q + q*q, count // 2)
    else:
        return fib_iter(b*q + a*q + a*p, b*p + a*q, p, q, count - 1)
    

n = 2_000_000 
func =  [fib_exp, fib_linear]
result = ''
for f in func:
    start_time = time.time()
    print(f(n))
    print("=====================")
    result += f"{f.__name__:<10}: {(time.time() - start_time) * 1000: .3f} msec\n"

print(result)
