CNP = input("Introduceti CNP-ul: ")
sec_20 = [1,2,7,8,9]
numar_control = list('279146358279')
global valid

def luna(cnp):
    if int(cnp[3]+cnp[4]) < 12:
        return cnp[3]+cnp[4]
    else: return 'invalid'

def judet(cnp):
    if int(cnp[7]+cnp[8]) in [50, 51] or int(cnp[7]+cnp[8]) < 47:
        return cnp[7]+cnp[8]
    else: return " nu este valid"


def zi(cnp):
    if int(cnp[3]+cnp[4]) in [1,3,5,7,8,10,12 ] and int(cnp[5]+cnp[6]) <=31:
        return cnp[5]+cnp[6]
    elif int(cnp[3]+cnp[4]) in [4,6,9,11] and int(cnp[5]+cnp[6]) <=30:
        return cnp[5] + cnp[6]
    elif int(cnp[3]+cnp[4]) in [2] and int(cnp[5]+cnp[6]) <=28 and int(cnp[1]+cnp[2]) % 4 != 0:
        return cnp[5] + cnp[6]
    elif int(cnp[3] + cnp[4]) in [2] and int(cnp[5] + cnp[6]) <= 29 and int(cnp[1] + cnp[2]) % 4 == 0:
        return cnp[5] + cnp[6]
    else: return "Ziua nu este valida"

def sex(cnp):
    if int(cnp) != 0:
        for i in [1,2,3,4,5,6,7,8,9]:
            # print(i)
            # print(S[i])
            if i == int(cnp[0]):
                return cnp[0]
    else: return "Nu este valid"

def nnn(cnp):
    if cnp[9]+cnp[10]+cnp[11] != '000':
        return cnp[9]+cnp[10]+cnp[11]
    else: return 'Invalid'

def cifra_control(cnp):
    cifra = 0
    for i, v in enumerate(numar_control):
        cifra = cifra + ((int(numar_control[i])) * (int(list(cnp)[i])))
    if cifra % 11 == 10:
        return  1
    elif cifra % 11 != 10:
        return  cifra % 11


if int(CNP[12]) == cifra_control(CNP) and zi(CNP).isdigit() and luna(CNP).isdigit() and nnn(CNP).isdigit() and judet(CNP).isdigit():
    print(f"Cnp-ul este valid")
else:
    print("Cnp-ul nu este valid")