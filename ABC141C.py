"""
全部でQ回の正解数
参加者iが正解した数をx回とすると、iのポイントは K-(Q-x) = K-Q+x
勝ち抜ける必要十分条件は、K-Q+x>0 ↔︎ x>Q-K
"""
from collections import Counter
n,k,q = map(int,input().split())
a = [int(input()) for _ in range(q)]
x = Counter(a)
for i in range(1,n+1):
  print("Yes" if x[i]>q-k else "No")
