"""
整数組 (i,j) (1≤i<j≤N) は N×(N−1)/2 個存在しますが、それらから Ai​ = Ajとなるものを引き去ることを考えます。
数列Aに含まれる整数 p について、 p が q 個含まれるなら、答えから q×(q−1)/2を減算する。
これは、 Ai = Aj = p となる整数組 (i,j) (i<j) の個数である。
"""

from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a.sort()
x = Counter(a)
ans = n*(n-1)//2
for i in x.values():
  ans -= i*(i-1)//2
print(ans)