# Zbadaj czy na liście licz A, znajdują się dwie liczby – a i b, których suma wynosi liczbę L.
#
# Czyli przykładowo, mamy podaną listę A = [1,3,5,2,11,7] . Należy sprawdzić czy suma, którychkolwiek liczb na liście wynosi 9. W tym prostym przykładnie już ‘na oko’ widzimy że będą to liczby 2 oraz 7. No dobrze, ale zastanówmy się jak mógłby wyglądać nasz algorytm.



def sum_of_number_is_number(lista,num):
    return_list = []
    help_list=[]
    for x in lista:
        for y in lista:
            if x+y==num:
                return_list.append([x,y])
    return return_list
num = 7
lista = [1,3,2,11,7,8,5]
print(sum_of_number_is_number(lista,num))

