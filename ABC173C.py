# h,wの制約が緩いし、行と列をそれぞれ塗るか、YesかNoかで答える
# ∴bit全探索
# 黒いマスになる条件は、
# ①元から黒い'#'
# ②その行が赤く塗られていない
# ③その列が赤く塗られていない
from itertools import product
h,w,k = map(int,input().split())
l = [list(input()) for _  in range(h)]
ans = 0
for i in product(range(2),repeat=h): #塗らないを0(False)、塗るを1(True)としてbit全探索する
  for j in product(range(2),repeat=w):
    c = 0
    for row in range(h):
      for col in range(w):
        if l[row][col]=="#" and (i[row] and j[col]):
          c += 1 #塗った後の黒マスを数える
    if c==k: #kと黒いマスの数が一致してたら++
      ans += 1
print(ans)