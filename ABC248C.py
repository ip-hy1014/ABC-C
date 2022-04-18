"""
dp[i][j] : 数列の i 番目まで決めて、総和が j であるものの数
"""
n,m,K = map(int,input().split())
mod = 998244353
dp = [[0]*(K+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
  for j in range(K):
    for k in range(1,m+1):
      if j+k>K:
        break
      dp[i+1][j+k]+=dp[i][j]
      dp[i+1][j+k]%=mod
print(sum(dp[-1])%mod)