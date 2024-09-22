numar = int(input("Introduceti numarul: "))
if numar > 0 and numar < 10:
    print(f"{numar} este pozitiv si mai mic decat zero")
elif numar > 0:
    print(f"{numar} este pozitiv, dar mai mare decat zero")
elif numar == 0:
    print("Numarul este 0")
elif numar < 0:
    print(f"{numar} este negativ, iar valoarea lui in modul este {abs(numar)}")