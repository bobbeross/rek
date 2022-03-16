# Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’, liczby podzielne przez 5, zastąp słowem ‘Buzz’, natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
#
# A w rezultacie, powinniśmy otrzymać – 1, 2, Fizz, 4, Buzz, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16 itd

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('fuzzbuzz')
    if x % 3 == 0:
        print('fuzz')
    if x % 5 == 0:
        print('buzz')
    else:
        print(x)
