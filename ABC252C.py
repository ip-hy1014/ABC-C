def f(x):
  d = n #残りリール数
  for t in range(1<<60): #適当に大きい数
    if c[x][t%10]>0: #止めてないリールがあったら止める
      c[x][t%10] -= 1
      d -= 1
    if d == 0: #リールが全て止まった時点のt秒を返す
      return t
n = int(input())
s = [input() for _ in range(n)]
c = [[0]*10 for _ in range(10)] #c[i][j]: 数字iがsのj番目に出てくる回数
for i in range(n):
  for j in range(10):
    c[int(s[i][j])][j] += 1
print(min(f(i) for i in range(10))) #全探索して一番小さいやつを出力