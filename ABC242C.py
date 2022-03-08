n = int(input())
mod = 998244353
dp = [[0]*11 for _ in range(n+1)] #二次元目の長さを11にすることで、j=1,9の時の場合分けをなくす
for i in range(1,10):
  dp[1][i] = 1
for i in range(1,n):
  for j in range(1,10):
    dp[i+1][j] = (dp[i][j-1] + dp[i][j] + dp[i][j+1]) % mod
print(sum(dp[n])%mod)
