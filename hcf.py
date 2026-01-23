import time

start  = time.time()

# Euclid's method O(log(min(a, b)))
a = 874
b = 598
hcf = 0

# a=bq+r

while True:
    q = a/b
    r = a%b
    a = b*q+r
    if r==0:
        break
    a = b
    b = r

hcf = b

print(hcf)

end = time.time()
print(f"Time taken: {end-start} ms")
