CNP = input("Introduceti CNP-ul: ")
sec_20 = [1,2,7,8,9]
numar_control = list('279146358279')

def cifra_control(cnp):
    cifra = 0
    for i, v in enumerate(numar_control):
        cifra = cifra + ((int(numar_control[i])) * (int(list(cnp)[i])))
    if cifra % 11 == 10:
        return  1
    elif cifra % 11 != 10:
        return  cifra % 11

if int(CNP[12]) != cifra_control(CNP):
    print("Cnp-ul nu este valid")
elif int(CNP[12]) == cifra_control(CNP):
    print(f"Cnp-ul este valid")