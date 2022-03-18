s = input()
l = len(s)
mod1 = 0
mod2 = 0
for i in range(l):
  n = int(s[i])
  mod = n%3
  if mod==1:
    mod1+=1
  if mod==2:
    mod2+=1
n = int(s)
if n%3==0:
  print(0)
elif n%3==1:
  if l>=2 and mod1>=1:
    print(1)
  elif l>=3 and mod2>=2:
    print(2)
  else:
    print(-1)
else:
  if l>=2 and mod2>=1:
    print(1)
  elif l>=3 and mod1>=2:
    print(2)
  else:
    print(-1)

#bit全探索
from itertools import product

# とりあえず文字列Sで受け取ったあと、桁ごとの数字のリストAにすると扱いやすいです
# N = 6227384 -> A = [6,2,2,7,3,8,4]

S = input()
A = [int(x) for x in S]

l = len(S)  # Sの桁数です（Sは文字列で受け取ったので、len(S)を使えます）
ans = l

for bits in product((True, False), repeat=l):
    digit_sum = 0  # 消してない桁の和です
    score = 0  # 桁を消した数で、少ないほうがうれしいです
    for i, bit in enumerate(bits):
        if bit:
            # 上からi桁目を消さずに使います
            digit_sum += A[i]
        else:
            # 上からi桁目を消します
            score += 1

    if digit_sum % 3 == 0:
        #  3の倍数になる消し方なら、最小値を更新します
        ans = min(ans, score)

if ans == l:
    # 3の倍数にならなかったので、-1を出力します
    print(-1)
else:
    print(ans)