#アナグラムかの判定はソートして確かめる
n = int(input())
d = {}
ans = 0
for _ in range(n):
  s = sorted(input())
  s = "".join(s)
  if s in d:
    d[s] += 1
    ans += d[s]
  else:
    d[s] = 0
print(ans)