n,m = map(int,input().split())
L = []
R = []
for i in range(m):
  l,r = map(int,input().split())
  L.append(l)
  R.append(r)
mx = max(L)
mn = min(R)
print(mn-mx+1 if mx<=mn else 0)