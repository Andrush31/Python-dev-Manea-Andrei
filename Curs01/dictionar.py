dictionar= {
    1: "ana",
    '2': "mere",
    '3': "pere",
    '4': "prune",
    '1': "Antonia"

}
# print(dictionar[2])
# print(dictionar[22])
# print(dictionar.get("22", "nu gaseste nimic"))
# dictionar["22"] = "Valoare noua"
dictionar.update({"22": "Valoare noua", "33": 'Alta valoare'})
print(dictionar.keys())
print(dictionar.items())
print(dictionar)