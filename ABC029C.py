import itertools
n = int(input())
for ans in itertools.product("abc",repeat=n):
  print("".join(ans))

#golf
from itertools import*
for i in product("abc",repeat=int(input())):
  print("".join(i))
