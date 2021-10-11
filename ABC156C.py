n = int(input())
x = list(map(int,input().split()))
l = []
for i in range(1,101):
  c = 0
  for j in range(n):
    c += (x[j]-i)**2
  l.append(c)
print(min(l))