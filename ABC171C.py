n = int(input())
# 数値→アルファベット
def a(n):
  if n<=26:
    return chr(64+n)
  elif n%26==0:
    return a(n//26-1)+chr(90)
  else:
    return a(n//26)+chr(64+n%26)
print(a(n).lower())

# アルファベット→数値
def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num


"""
数値からアルファベットの変換は10進数→26進数的な考え方を使います。

例えば、『1000』という数値をアルファベットに変換させる場合、

26のn乗で1000以下の最大のnを求める→『n+1』がアルファベットの桁数、n=2
(26^2)*xで1000以下の最大のxを求める→x=1、つまり3桁目のアルファベットはA
(26^1)*yで1000-(26^2)*1=324以下の最大のyを求める→y=12、つまり2桁目のアルファベットはL
(26^0)*z=12→つまり3桁目のアルファベットはL、ゆえに1000はALL
"""