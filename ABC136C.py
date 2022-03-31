n = int(input())
h = list(map(int,input().split()))
mx = -1
ans = "Yes"
for i in range(n):
  mx = max(mx,h[i])
  if mx-h[i]>1:
    ans = "No"
print(ans)