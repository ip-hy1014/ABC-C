n = int(input())
v = list(map(int,input().split()))
v.sort()
a = (v[0]+v[1])/2
for i in range(2,n):
  a = (v[i]+a)/2
print(a)