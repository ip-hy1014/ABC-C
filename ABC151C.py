n,m = map(int,input().split())
ac = [True]*n
wa = [0]*n
AC = 0
WA = 0
for _ in range(m):
  p,s = list(input().split())
  p = int(p)-1
  if s=="AC" and ac[p]:
    WA += wa[p]
    AC += 1
    ac[p] = False #同じ問題でACしても重複してカウントしないように
  else:
    wa[p] += 1
print(AC,WA)