"""
SとTに含まれる#の個数が異なればNo
90度の回転は(x,y)→(y,-x)に置き換えれば良い
グリッドの状態を#の位置の集合として持つ
"""

n = int(input())
# グリッドを読み込んで#の位置の集合を返す
def read():
  s = set()
  for y in range(n):
    u = input()
    for x in range(n):
      if u[x]=="#":
        s.add((x,y))
  return s
s = read()
t = read()
#90度回転の回数を全探索(4回)、それに対応する平行移動の仕方は1通り
for _ in range(4):
  # 最も左（複数あればそのうちで最も上）の#を(0, 0)の位置にする
  ml_x,ml_y = min(s)
  s = set((x-ml_x,y-ml_y) for x,y in s)
  ml_x,ml_y = min(t)
  t = set((x-ml_x,y-ml_y) for x,y in t)
  if s==t:
    print("Yes")
    exit()
  # Tを回転
  t = set((y,-x) for x,y in t)
print("No")