n,k = map(int,input().split())
ans = k
l = [list(map(int,input().split())) for _ in range(n)]
l.sort()
for i in range(n):
  if ans < l[i][0]: #所持金が一番最初の村に辿り着ける金額未満だったら終了
    break
  else:
    ans += l[i][1] #村に辿り着けたらお金が増える
print(ans)
