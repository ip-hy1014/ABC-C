s = input()
ans = 0
for i in range(10**4): #4桁の文字列なので全部で10**4
  flg = True
  t = str(i).zfill(4) #0埋めすることで暗証番号を実現
  for j in range(10):
    if s[j]=="o":
      if str(j) not in t:
        flg = False
    if s[j]=="x":
      if str(j) in t:
        flg = False
  if flg==True:
    ans += 1
print(ans)