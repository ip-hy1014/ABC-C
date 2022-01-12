# Nから見ていってNの習得に必要な頂点の習得に必要な時間の合計が答え
def dfs():
  seen = [False]*(n+1)
  stack = [n]
  seen[n] = True
  ans = 0
  while stack:
    u=stack.pop()
    ans+=t[u]
    for v in g[u]:
      if not seen[v]:
        seen[v]=True
        stack.append(v)
  return ans

n = int(input())
t = [0]*(n+1)
g = [[] for _ in range(n+1)]
for u in range(1,n+1):
  t[u],k,*a = map(int,input().split())
  for v in a:
    g[u].append(v)
print(dfs())