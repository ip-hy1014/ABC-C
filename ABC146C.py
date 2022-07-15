#二分探索
a,b,x = map(int,input().split())
mx = 10**9+1
mn = 0
while mx-mn>1: # >1 にせずにたとえば >0 にすると同じ計算をずっとしてしまう
  z = (mx+mn)//2
  if a*z+b*len(str(z))<=x:
    mn = z
  else:
    mx = z
print(mn)