import random


# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# # the lambda function returns True for even numbers
# even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
#
# # converting to list
# even_numbers = list(even_numbers_iterator)
#
# print(even_numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# # the lambda function returns True for even numbers
# even_numbers_iterator = map(lambda x: (x%2 == 0), numbers)
#
# # converting to list
# even_numbers = list(even_numbers_iterator)
#
# print(even_numbers)
# from functools import reduce
#
# numbers = [1, 2, 3, 4]
#
# # the lambda function returns True for even numbers
# even_numbers_iterator = reduce((lambda x,y: x*y), numbers)
#
# # converting to list
#
# print(even_numbers)


# a=[1,2,3]
# b=a.copy()
# c=a
# a[0]=10
# print(f'a:{a} b:{b} c:{c}')

# t = (1, 2, 3, 4)
# t[0] = 8
# print(t)

# t = (1, 2, 3, 4)
# t.append(5)
# print(t)

# t = "hehe"
# w = t*5
# print(w)

# t = {}
# print(type(t))

# t = {}
# t[1] = 10
# t[199] = 'c'
# print(t)

# a = [1, 2, 3]
# b=a
# b[2] = 10
# print(a)
# print(b)

# L = [1,2,3]
# for element in L:
#     element =  print(L)


# L = [1,2,3]
# for i in range(len(L)):
#     L[i] = print(L)

# if True:
#     x = 10
# print(x)

# for i in range (5): pass
# print(i)

# def f(): print(a)
# a=8
# f()


# def f():
#     a = 15
# a=8
# f()
# print(a)


# def f():
#     global a
#     a=11
#
# a = 15
# a=8
# f()
# print(a)

# def f(): global a
# a = 15
# a=8
# print(a)


# def f(L1):
#     L1 [0] = 15
# L = [1,2,3]
# f(L)
# print(L, L1)


# def f(L1): L = L1
# L = [1,2,3]
# f([4,5,6])
# print(L)

# def f(L1): global L
# L = L1
# L = [1,2,3]
# f([4,5,6])
# print(L)

# def f(L1):
#     global L
#     L = L1[:]
#
# L = [1,2,3]
# L[0] = 15
# f([4,5,6])
# print(L)

# def f(L1):
#     L = L1[:]
#
# L = (1,2,3)
# L[0] = 15
# f((4,5,6))
# print(L)

def zad15(s):
    unique = sorted(set(s))
    for x in unique:
        print(f' {x} count: {s.count(x)}')

# zad15('aabbccajsdisdfbjsdbf')


def zad10(a,b):
    lis =[]
    for x in range(5):
        lis.append(random.uniform(a,b))
        print(f'x: {x} lis: {lis[x]}')
    print(f'count: {len(lis)}')
    print(f'max: {max(lis)} id: {lis.index(max(lis))}')

# zad10(-1,1)


import datetime
def imd(rrrr,mm,dd):
    return (datetime.datetime.now()-datetime.datetime(rrrr,mm,dd)).days

# print(imd(1993,1,8))




def kiedy(x, y):
    long = 1000
    day = 0
    while long > 0:
        long -= x
        if long<0:
            return day
        long += y
        day += 1


# print(kiedy(4, 2))
