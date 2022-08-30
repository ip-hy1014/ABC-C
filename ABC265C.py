#訪問済かどうかを管理して、既にTrueになっている箇所を再び通ろうとした場合に-1を出力する
h,w = map(int,input().split())
g = [input() for _ in range(h)]
i = 0 #スタート地点を(0,0)とする
j = 0
visit = [[False]*w for _ in range(h)] #訪問フラグ管理
while True:
  if visit[i][j]: #訪問済の地点を再度通過したら無限ループしてるので-1を出力
    print(-1)
    exit()
  visit[i][j] = True
  x = i
  y = j
  if g[i][j]=="U":
    i-= 1
  elif g[i][j]=="D":
    i += 1
  elif g[i][j]=="L":
    j -= 1
  else:
    j += 1
  if i==-1 or j==-1 or i==h or j==w:
    print(x+1,y+1) #題意を満たすように+1する
    exit()