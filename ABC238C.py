def s(x):
  return x*(x+1)//2
n = int(input())
mod = 998244353
l = len(str(n))
ans = 0
for i in range(l-1):
  ans += s(9*10**i) #n-1桁目までの合計値
ans += s(n-10**(l-1)+1) #残りの合計値
print(ans%mod)

#別解
def s(x):
  return x*(x+1)//2
n = int(input())
mod = 998244353
l = len(str(n))
ans = 0
for i in range(1,l+1):
  k = min(n,10**i-1)-(10**(i-1)-1)
  ans += s(k)
  ans %= mod
print(ans)

"""
d(j)をj桁以下の整数の数とすると、ki = min(n,d(i))-d(i-1)
4桁の整数 1000~9999 は9000個ある
n=10**15
k = min(10**15,9999)-999 = 9000
n=1234
k = min(1234,9999)-999 = 235
"""
