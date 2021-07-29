a,b,c,x,y = map(int, input().split())
ans = float("INF")
for i in range(10**5+1):
  j = max(x-i,0)
  k = max(y-i,0)
  t = 2*c*i + a*j + b*k
  ans = min(ans,t)
print(ans)