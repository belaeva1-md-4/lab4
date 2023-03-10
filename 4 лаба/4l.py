
"eett"
def s1():
    print("Введите число")
    x=int(input())
    if x%3==0:
        print("Делится")
    else:
        print("Не делится")


def s2():
    print("Введите число")
    c=int(input())
    try:
        res= 100 / c
        print(res)
    except ValueError:
        print("Вы ввели строку")
    except ZeroDivisionError:
        print("Деление на 0")

s1(), s2()



