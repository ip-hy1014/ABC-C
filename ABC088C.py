c = [list(map(int,input().split())) for _ in range(3)]
ok = True
if c[0][0] - c[0][1] != c[1][0] - c[1][1] or c[1][0] - c[1][1] != c[2][0] - c[2][1]:
  ok = False
if c[0][1] - c[0][2] != c[1][1] - c[1][2] or c[1][1] - c[1][2] != c[2][1] - c[2][2]:
  ok = False
if c[0][0] - c[1][0] != c[0][1] - c[1][1] or c[0][1] - c[1][1] != c[0][2] - c[1][2]:
  ok = False
if c[1][0] - c[2][0] != c[1][1] - c[2][1] or c[1][1] - c[2][1] != c[1][2] - c[2][2]:
  ok = False
if ok:
  print("Yes")
else:
  print("No")