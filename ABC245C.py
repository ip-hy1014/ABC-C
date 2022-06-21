#考え方としてはDPを用いる
#あくまで隣接する要素のみを見れば良いため、2つ前の要素はどうでも良い
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [a[0],b[0]] #隣接する要素が条件を満たすかを記録するための配列,最初はaかbのどちらかの先頭の要素と比較するところからスタート
for i in range(n):
  s = set()
  for x in c:
    if abs(x-a[i])<=k:
      s.add(a[i])
    if abs(x-b[i])<=k:
      s.add(b[i])
  c = s #ここで次の要素と比較するための要素を記録する
print("Yes" if c else "No")
