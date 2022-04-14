n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [0]*(n+1)
c = 0
for i in range(n):
  c += a[i]
  dp[i+1] = max(dp[i]+b[i],c+b[i])
print(dp[n])