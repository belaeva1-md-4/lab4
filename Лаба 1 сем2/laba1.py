password1 = str(input())
password2 = str(input())

if password1!=password2:
    print("пароли не совпадают")
else:
    if len(password1)<5:
        print("пароль слишком короткий")
    else:
        print("пароль принят")





