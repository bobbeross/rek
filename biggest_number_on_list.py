# Zadanie jest następujące. Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
#
# Czyli, dla przykładu, jeżeli nasza lista to:
#
# lista = [1,4,-4,7]
#
# To najmniejsza liczba wynosi -4, natomiast największa 7.

def biges_number_on_list(list):
    return max(list)


def smallest_number_on_list(list):
    return min(list)


list = [1, 2, 8, 3, 4, 5, 6]
print(biges_number_on_list(list))
print(smallest_number_on_list(list))
