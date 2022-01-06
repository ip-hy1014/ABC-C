from itertools import *
n,x = map(int,input().split())
l = [list(map(int,input().split()[1:])) for _ in range(n)]
ans = 0
for i in product(*l):
  c = 1
  for j in i:
    c *= j
  if c==x:
    ans+=1
print(ans)

#dfs
from sys import setrecursionlimit
setrecursionlimit(10**7)
def rec(bag_i,all_product):
    """bag_i番目の袋からボールを選ぶ"""
    # すべての袋から1つづつボールを選び終わった場合
    if bag_i >= n:
        if all_product == x:
            return 1
        else:
            return 0
    # まだボールを選んでいない袋がある場合
    res = 0
    for i in l[bag_i]:
        res += rec(bag_i+1,all_product*i)
    return res

n,x = map(int,input().split())
# 入力は数列Aだけ欲しいので、Lは捨てている
l = [list(map(int,input().split()[1:])) for _ in range(n)]
print(rec(0,1))
