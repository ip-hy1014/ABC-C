n,m = map(int,input().split())
s = [input() for _ in range(2*n)]
rank = [[0,i] for i in range(2*n)] #[勝利数,選手番号]
def judge(a,b):
  if a==b: return -1
  if a=="G" and b=="P": return 1
  if a=="C" and b=="G": return 1
  if a=="P" and b=="C": return 1
  return 0
for j in range(m):
  for i in range(n):
    p1 = rank[2*i][1]
    p2 = rank[2*i+1][1]
    r = judge(s[p1][j],s[p2][j])
    if r != -1:
      rank[2*i+r][0] -= 1 #勝った人に+1ポイントするかわりに、−1ポイントすることにすると、普通にソートするだけで順位通りに並び替えられる
  rank.sort()
for _,i in rank:
  print(i+1)