nom=int(input())
if nom>36 and nom <54:
    if nom%2==0:
        print("У вас боковое верхнее")
    else:
        print(" вас боковое нижнее")
elif nom >54:
    print("такого места нет")
elif nom%2==0:
    print("У вас верхнее в купе")
else:
    print("У вас нижнее в купе")
