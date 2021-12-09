#ソートして貪欲
n,w = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x: -x[0])
ans = 0
for a,b in ab:
  mn = min(w,b)
  ans += a*mn
  w -= mn
print(ans)