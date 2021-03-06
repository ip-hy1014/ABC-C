"""
全ての数列の数から条件を満たさない数列の数を引けば良い
A = 全ての数列の数:0~9を並べるので10**n通り
B = 0を使わない数列の数:0以外の9個の数字を並べるので9**n通り
C = 9を使わない数列の数:同上
答え:A-B-C+(BとCの重複部分)
"""

n = int(input())
mod = 10**9+7
ans = pow(10,n,mod)
ans -= 2*pow(9,n,mod)
ans += pow(8,n,mod)
print(ans%mod)