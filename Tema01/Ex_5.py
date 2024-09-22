dict_alegeri ={1: "Afisare lista de cumparaturi",
2: "Adaugare element",
3: "Stergere element",
4: "Sterere lista de cumparaturi",
5: "Cautare in lista de cumparaturi"}
g = 1
confirmare = input("Ati selectat meniul nostru, doriti sa continuati catre optiuni? \n 1 - Da \n 2 - Nu\n")
if confirmare == "1":
    while g != 0:
        print("Alegeti optiunea pe care o doriti: ")
        for key, value in dict_alegeri.items():
            print(f"{key} - {value}")
        numar = int(input())
        for j, k in dict_alegeri.items():
            if j == numar:
                print(f"Ati selectat optiunea '{k}'")
            elif numar > 5 or numar < 1:
                print('Alegerea nu exista. Reincercati!')
                break
        confirmare_2 = input("Ati dori sa alegeti alta optiune? \n 1 - Da \n 2 - Nu\n")
        if confirmare_2 == "2":
            print("Va multumim si la revedere!")
            g -= 1

elif confirmare != "1":
    print("Va multumim si la revedere!")