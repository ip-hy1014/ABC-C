#(i*j)%2019 = (i%2019) * (j%2019) % 2019
#∴ どっちかが 2019の倍数なら答えは0にる。
#if R−L>=2019 なら、L から R までの間に2019の倍数が存在することになり、答えは0
#else とりうるバターン数は 2019^2 以下におさまるので、全探索可能
l,r = map(int,input().split())
ans = 1<<60
if r-l>=2019:
  print(0)
else:
  for i in range(l,r):
    for j in range(i+1,r+1):
      ans = min(ans,(i*j)%2019)
  print(ans)