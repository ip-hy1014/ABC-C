n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [a[0],b[0]]
for i in range(n):
  s = set()
  for x in c:
    if abs(x-a[i])<=k:
      s.add(a[i])
    if abs(x-b[i])<=k:
      s.add(b[i])
  c = s
print("Yes" if c else "No")