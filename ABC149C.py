n = int(input())
def isprime(n):
    i = 2
    if n==1:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
while not isprime(n):
  n+=1
print(n)