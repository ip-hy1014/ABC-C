n,k = map(int,input().split())
p = [0]*n
for i in range(n):
  p[i] = sum(map(int,input().split()))
t = sorted(p,reverse=True)[k-1]
for i in p:
  print("Yes" if i+300>=t else "No")