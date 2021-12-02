"""
湖の周りを家によってN個の区間に分ける
N個の区間のうち通らないものは高々1個
そのうち一番長い区間を通らないようにする
湖の円周Kmから隣り合う家の距離a[i+1]-a[i]を引くと全ての家を訪ねた移動距離になり、この値が一番小さいものが答え
"""
k,n = map(int,input().split())
a = list(map(int,input().split()))
ans = a[n-1]-a[0]
for i in range(n-1):
  ans = min(ans,k-a[i+1]+a[i])
print(ans)