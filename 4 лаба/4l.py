

def N(x):
    if x%3==0:
        return True
    else:
        return False

c=int(input())
if N(c):
    print("Делится")
else:
    print("Не делится")