c=str(input())
l=len(c)

a=int(c[0:((l//2))])
b=int(c[((l//2)):(l)])
s1=0
s2=0
d=0

while a>0:
    d=a%10
    s1=s1+d
    a=a//10
while b>0:
    b=b%10
    s2=s2+d
    b=b//10

if s1==s2:
    print("Оно счастливое")
else:
    print("Не счастливое")