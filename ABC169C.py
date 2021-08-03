#浮動小数点数として掛け算を行うと精度不足
a,b = map(float,input().split())
print(int(a)*round(b*100)//100)