n,k = map(int,input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = 1<<60
for i in range(n-k+1):
  mn = h[i]
  mx = h[i+k-1]
  ans = min(ans,mx-mn)
print(ans)