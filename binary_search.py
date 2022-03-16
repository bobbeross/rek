# Wyszukiwanie binarne, to algorytm mający na celu sprawdzenie czy podany element znajduje się na posortowanej liście liczb oraz wskazanie jego miejsca. Działa w czasie logarytmicznym co nabiera znaczenia w przypadku dużych zbiorów danych.
# Aby sprawdzić czy liczba L znajduje się w 1000 elementowej liście, przy zastosowaniu standardowej pętli typu For, w najgorszym przypadku potrzebujemy 1000 iteracji. Po prostu, musieli byśmy sprawdzać element po elemencie.
#
# Z użyciem algorytmu wyszukiwania binarnego, 10.
#
# Dla tablicy 1 000 000 elementów, pętla For potrzebuje w najgorszym przypadku 1 000 000 iteracji, algorytm wyszukiwania binarnego, 20.
#
# Tak jak widzimy różnica jest olbrzymia. Jak ją osiągnąć?
#
# Fundamenty działania algorytmu:
#
# zbiór jest posortowany, w naszym przypadku, lista liczb
# algorytm dzieli ją na dwie równe listy
# sprawdza czy znalazł szukaną liczbę. Jeżeli nie, to sprawdza w który zbiór zawiera zakres liczb poszukiwanych. Czyli jeżeli widzi, że w zbiorze na lewo są liczby mniejsze, to nie zajmuje się szukaniem w tym zbiorze, tylko sprawdza zbiór
# znowu, dzieli go na 2 równie zbiory
# znowu sprawdza czy znalazł, znowu szukaną liczbę, dzieli zbiór itd.
#
# Praktyczna porada:
#
# Jest to kolejne zadanie, które jest o wiele łatwiejsze, jeżeli zanim zaczniemy programować, rozrysujemy je na kartce.
def search_number_in_list(list, number):
    list.sort()
    left = 0
    right = len(list)
    list_ = []
    while True:
        idx = (right + left) // 2
        if list[idx] == number:
            return idx
        elif list[idx] > number:
            right = idx
        elif list[idx] < number:
            left = idx
        list_.append(idx)
        if len(list_)>2:
            if list_[-1]==list_[-2]:
                return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 15, 11, 20]
print(search_number_in_list(list, 21))
