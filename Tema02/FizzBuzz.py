while True:
    nr = input("Introdu numarul: ")
    nr = int(nr)
    if nr % 3 == 0 and nr % 5 == 0:
        print("FizzBuzz")
    elif nr % 3 == 0:
        print("Fizz")
    elif nr % 5 == 0:
        print("Buzz")
    elif nr % 3 != 0 and nr % 5 !=0:
        print(nr)