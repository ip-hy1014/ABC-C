# 予め最大値と2番目に大きい値を取得しておく
n = int(input())
a = []
for _ in range(n):
  a.append(int(input()))
b = sorted(a)[::-1]
c = b[0]
d = b[1]
for i in a:
  if i == c:
    print(d)
  else:
    print(c)