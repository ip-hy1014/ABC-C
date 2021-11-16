n = int(input())
h = list(map(int,input().split()))
ans = 0
c = 0
for i in range(n-1):
  if h[i] >= h[i+1]:
    c += 1
  else:
    ans = max(c,ans)
    c = 0
print(max(ans,c))