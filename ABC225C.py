"""
横に+1,縦に+7,7の倍数は一番右端にないとダメ
"""

n,m = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(n)]
v = True
for i in range(n):
  for j in range(m):
    if j+1 < m and b[i][j]+1 != b[i][j+1]: #m列以内かつ横に+1したものになっているか
      v = False
    if i+1 < n and b[i][j]+7 != b[i+1][j]: #n行以内かつ縦に+7したものになっているか
      v = False
    if b[i][j]%7==0 and j!=m-1: #7の倍数が右端になっているか
      v = False
print("Yes" if v else "No")