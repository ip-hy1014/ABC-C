#積が最大となるのは差が最小のとき
n = sorted(input())[::-1]
a = n[::2] #奇数番目
b = n[1::2] #偶数番目
for i in range(min(len(a),len(b))):
  if a[i]!=b[i]:
    a[i],b[i] = b[i],a[i]
    break
print(int("".join(a))*int("".join(b)))