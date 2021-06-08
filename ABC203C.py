n,k = map(int, input().split())
l = []
for i in range(n):
  a,b = map(int, input().split())
  l.append([a,b])
l.sort() #村を近い順にソートする
ans = k #絶対所持金分は進める
for i in range(n):
  if ans < l[i][0]: #所持金が一番最初の村に辿り着ける金額未満だったら終了
    break
  else:
    ans += l[i][1] #村に辿り着けたらお金が増える
print(ans)