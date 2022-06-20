"""
2マスが決まれば残りの1マスは一意に定まる
→左上2*2の範囲を全探索する
"""
h = list(map(int,input().split()))
ans = 0
for i in range(1,31):
  for j in range(1,31):
    for k in range(1,31):
      for l in range(1,31):
        a = h[0]-i-j
        b = h[1]-k-l
        c = h[3]-i-k
        d = h[4]-j-l
        e = h[5]-a-b
        f = h[2]-c-d
        if a>0 and b>0 and c>0 and d>0 and e>0 and e==f:
          ans += 1
print(ans)