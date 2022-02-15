import sys
sys.setrecursionlimit(10**6)
n = int(input())
# child[i]:頂点iの子（部下）となる頂点たち
child = []
for _ in range(n):
  child.append([]) # 木構造の表現
for i in range(1,n):
  b = int(input())
  child[b-1].append(i)
# dfs(i):頂点iの子の給料を全て求め、自身の給料を計算して返す
def dfs(i):
  # 子がいなければ1
  if len(child[i])==0:
    return 1
  else:
    values = []
    for j in child[i]:
      values.append(dfs(j))
    return max(values) + min(values) + 1
print(dfs(0))