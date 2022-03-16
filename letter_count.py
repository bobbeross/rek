# Bardzo popularnym zadaniem, szlifującym nasz język, jest program do analizy ciągu znaków, czyli przykładowo zliczenia liczby słów czy też znaków.
#
# Mamy podany ciąg S. Np „Ala ma kota”. W ramach zadania możemy zostać poproszeni o jedno, lub więcej z poniższych:
#
# 1. zliczyć wyrazy. W naszym przypadku będzie ich 3
#
# 2. zliczyć litery. Będzie ich 9
#
# 3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1


def counter(string):
    return f'words: {words_count(string)}, char: {letters_count(string)}, letters_countń: {letters_count_by_one(string)}'

def words_count(string):
    return len(string.split(" "))


def letters_count(string):
    return len(string.replace(" ", ""))


def letters_count_by_one(string):
    letters = string.replace(" ", "")
    seted = set(letters)
    letters_count = []
    for letter in seted:
        coun = ''.join(letters).count(letter)
        letters_count.append([letter, coun])
    return letters_count


print(counter("aa aadf, add, asd"))
