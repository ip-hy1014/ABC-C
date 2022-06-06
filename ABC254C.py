"""
iが同じグループの中で昇順になっていない要素の組があってはいけない
すべての 0≤i<K について、グループを昇順にソートする
これが一致してれば良い
"""
n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(k):
  a[i::k] = sorted(a[i::k])
print("Yes" if a==sorted(a) else "No")