luni = ('Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie',  'Noiembrie', 'Decembrie')
S = {
1: 'Barbat', 2: 'Femeie',
3: 'Barbat', 4: 'Femeie',
5: 'Barbat', 6: 'Femeie',
7: 'Barbat strain cu rezidenta in Romania',
8: 'Femeie straina cu rezidenta in Romania',
9: 'Persoana straina'}
# print(S)
Cod_judet = {
1:'Alba', 2:'Arad', 3:'Arges', 4:'Bacau', 5:'Bihor', 6:'Bistrita-Nasaud',
7:'Botosani', 8:'Brasov', 9:'Braila', 10:'Buzau', 11:'Caras-Severin',
12: 'Cluj', 13:'Constanta', 14:'Covasna',15:'Dambovita', 16:'Dolj',
17: 'Galati', 18:'Gorj', 19:'Harghita', 20:'Hunedoara', 21:'Ialomita',
22:'Iasi',23:'Ilfov',24:'Maramures',25:'Mehedinti',26:'Mures',27:'Neamt',
28:'Olt',29:'Prahova',30:'Satu-Mare',31:'Salaj',32:'Sibiu',33:'Suceava',
34:'Teleorman',35:'Timis',36:'Tulcea',37:'Vaslui',38:'Valcea',39:'Vrancea',
40:'Bucuresti',41:'Sector 1',42:'Sector 2',43:'Sector 3',44:'Sector 4',45:'Sector 5',
46:'Sector 6'}
CNP = input("Introduceti CNP-ul: ")
sec_20 = [1,2,7,8,9]
numar_control = list('279146358279')
# print(numar_control[3])
cifra = 0
# for i,v in enumerate(numar_control):
#     cifra = cifra + ((int(numar_control[i])) * (int(list(CNP)[i])))
    # print(cifra)
# cifrade = cifra % 11
def sex(cnp):
    for i in S:
        # print(i)
        # print(S[i])
        if i == int(cnp[0]):
            return S[i]

def an(cnp):
        if int(cnp[0]) in sec_20:
            return   '18' + cnp[1] + cnp[2]
        elif int(cnp[0]) in [3,4]:
            return '19' + cnp[1] + cnp[2]
        elif int(cnp[0]) in [5,6]:
            return '20' + cnp[1] + cnp[2]

def luna(cnp):
    return luni[int(cnp[3]+cnp[4]) - 1]

def judet(cnp):
    return Cod_judet[int(cnp[7]+cnp[8])]

def zi(cnp):
    return cnp[5]+cnp[6]

def nnn(cnp):
    return cnp[9]+cnp[10]+cnp[11]

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
    print(f"Cnp-ul apartine unui/unei {sex(CNP)}, nascut/a la data de {zi(CNP) + '. ' + luna(CNP) + ' .' + an(CNP)}\n "
          f" In judetul {judet(CNP)}, a fost a {nnn(CNP)} persoana nascuta, iar cifra de verificare este {cifra_control(CNP)}")
elif int(CNP[12]) == cifra_control(CNP):
    print(f"Cnp-ul apartine unui/unei {sex(CNP)}, nascut/a la data de {zi(CNP) + '. ' + luna(CNP)+ ' .' +an(CNP)}\n "
      f" In judetul {judet(CNP)}, a fost a {nnn(CNP)} persoana nascuta, iar cifra de verificare este {cifra_control(CNP)}")
# print(S[5])
# print(list(CNP)[0])
# print(an(CNP))
# haha = sex(CNP)
# print(haha)
# print(zi(CNP))
# print(luna(CNP))
# print(judet(CNP))
# print(cifra_control(CNP))

    #liniile comentate reprezinta etapele de progres ale codului