l = list(map(int,input().split()))
l.sort()
s = sum(l)
if s%2 != l[2]%2:
  l[2]+=1
print((3*l[2]-s)//2)