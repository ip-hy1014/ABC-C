#l,rの組を全探索して最大値を求める
n = int(input())
a = list(map(int,input().split()))
ans = 0
for l in range(n):
  mn = 1<<60 #十分な大きさで初期化
  for r in range(l,n):
    c = r-l+1 #区間の幅
    mn = min(mn,a[r])
    x = mn*c #食べたみかんの数
    ans = max(ans,x)
print(ans)