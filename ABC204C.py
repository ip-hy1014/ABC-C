#BFS（幅優先探索）
def main():
  from collections import deque

  def bfs(start):
    seen = [False] * n
    seen[start] = True
    que = deque((start,))
    while que:
      u = que.popleft()
      for v in edge[u]:
        if not seen[v]:
          seen[v] = True
          que.append(v)
    return seen.count(True)
  n,m = map(int, input().split())
  edge = [[] for _ in range(n)]
  for _ in range(m):
    a,b = (x-1 for x in map(int, input().split()))
    edge[a].append(b)
  ans = 0
  for i in range(n):
    ans += bfs(i)
  print(ans)

if __name__ == "__main__":
  main()