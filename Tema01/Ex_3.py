numar = int(input("Introduceti anul: "))
if numar % 4 == 0:
    print(f"{numar} este an bisect")
elif numar % 4 != 0:
    print(f"{numar} nu este an bisect")