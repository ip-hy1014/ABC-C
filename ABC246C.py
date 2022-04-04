n,k,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
  m = min(k,a[i]//x)
  a[i] -= m*x
  k -= m
a = sorted(a)[::-1]
for i in range(n):
  if k>0:
    a[i] = 0
    k -= 1
print(sum(a))