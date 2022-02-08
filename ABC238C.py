mod = 998244353
def f(x):
  return x*(x+1)//2
def s():
  n = int(input())
  l = len(str(n))
  ans = 0
  for i in range(1,l+1):
    k = min(n,10**i-1)-(10**(i-1)-1)
    ans += f(k)
    ans %= mod
  return ans
print(s())

"""
d(j)をj桁以下の整数の数とすると、ki = min(n,d(i))-d(i-1)
4桁の整数 1000~9999 は9000個ある
n=10**15
k = min(10**15,9999)-999 = 9000
n=1234
k = min(1234,9999)-999 = 235
"""