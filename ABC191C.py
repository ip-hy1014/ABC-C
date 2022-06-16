# 方針としては2*2の正方形領域を全探索して角の数を数えれば良い
h,w = map(int,input().split())
g = []
for _ in range(h):
  s = input()
  g.append(list(1 if i=="#" else 0 for i in s)) # #を1に、.を0に変換
ans = 0
for i in range(h-1):
  for j in range(w-1):
    c = 0
    c += g[i][j] #左上
    c += g[i+1][j] #左下
    c += g[i][j+1] #右上
    c += g[i+1][j+1] #右下
    if c==1: #ある点の周囲4マスのうち#が 1 or 3ならその点は角
      ans += 1
    if c==3:
      ans += 1
print(ans)