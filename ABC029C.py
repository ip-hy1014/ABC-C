import itertools
n = int(input())
for ans in itertools.product("abc",repeat=n):
  print("".join(map(str,ans)))