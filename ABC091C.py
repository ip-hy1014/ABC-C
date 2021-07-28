n = int(input())
r = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1]) #y座標で降順ソート
b = sorted([list(map(int, input().split())) for _ in range(n)]) #x座標で昇順ソート
ans = 0
for c,d in b:
  for a,b in r:
    if a<c and b<d:
      ans += 1
      r.remove([a,b]) #1つの点が複数のペアに所属することはできないため
      break
print(ans)