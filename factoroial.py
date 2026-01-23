import time

start  = time.time()

def Factorial(n):
    if n==0:
        return 1
    else:
        return n * Factorial(n-1)
    
print(Factorial(5))

end = time.time()
print(f"Time taken: {end-start} ms")
