# Problem: mamy podaną listaę liczb. Np. A = [2,1,5,3,6]. Należy posortować ją rosnąco, za pomocą algorytmu bąbelkowego.
#
# Sortowanie bąbelkowe: jest to prosta i najbardziej znana metoda sortowania. Polega ona na:
#
# ’przejściu’ przez poszczególne elementy lista, np za pomocą pętli 'for’,
# sprawdzeniu czy element następny na liście, jest mniejszy. Jeżeli tak, zastąpieniu ich miejscami.
# Powtarzamy czynność, dla kolejnego elementu i sprawdzamy czy kolejny jest mniejszy. Jeżeli tak, to zamieniamy miejscami, itd
# W momencie, kiedy dojdziemy do końca listay, na jej końcu powinna znajdować się największa liczba z listay,
# Następnie powtarzamy naszą pętlę 'for’, zaczynając od początku.
# kończymy wtedy, gdy wykonamy interakcję bez zmiany kolejności żadnego elementu
# Przykład:
#
# Iteracja 1: [2,0,5,1,6,3] (0<2) – > [0,2,5,1,6,3](5>2) → [0,2,5,1,6,3](1<5) → [0,2,1,5,6,3] (6>5)→[0,2,1,5,6,3](3<6) -> [0,2,1,5,3,6]
#
# Iteracja 2: [0,2,1,5,3,6] (1<2) → [0,1,2,5,3,6] (5>2) → [0,1,2,5,3,6] (3<5) → [0,1,2,3,5,6] (6>5) → [0,1,2,3,5,6]

def sort_buble(lista):
    while True:
        count = 1
        for idx, _ in enumerate(lista):
            if idx == len(lista) - 1:
                break
            if lista[idx] > lista[idx + 1]:
                lista[idx], lista[idx + 1] = lista[idx + 1], lista[idx]
                count += 1
        if count == 1:
            return lista


lista = [2, 1, 5, 7, 4, 3, 2, 5, 6, 99, 77, 66, 324234, 3]
print(lista)
print(sort_buble(lista))
