# Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
# Po dokonaniu wybory, Komputer odlicza 3,2,1, a następnie dokonuje 'rzutu’, czyli losowego wyboru orzeł / reszka.
# Komputer wyświetla wynik rzutu.
# Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
# Wyświetla wyniki
# Wracamy do punktu 1.
import random

player_points = 0
computer_points = 0
while True:
    coin = random.choice(['o', 'r'])
    inputt = input("Wybierz Orzel(o) lub Reszke(r): Exit(x): ").lower()
    if inputt not in ['o', 'r', 'x']:
        continue
    if inputt=='x':
        break
    if inputt==coin:
        player_points +=1
    else:
        computer_points +=1
    print(f'player_points: {player_points}, computer_points: {computer_points}')


