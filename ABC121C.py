n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[0])
ans = 0
for a,b in ab:
  if b<m:
    m -= b
    ans += a*b
  else:
    ans += m*a
    break
print(ans)