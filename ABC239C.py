a,b,c,d = map(int,input().split())
for x in range(a-3,a+3):
  for y in range(b-3,b+3):
    if (x-a)**2+(y-b)**2 == (x-c)**2+(y-d)**2 == 5:
      print("Yes")
      exit()
else:
  print("No")