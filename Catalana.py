def catalan_rec(n):
    b = 0
    if n == 0:
        return 1
    else:
        for i in range (n):
            b += (catalan_rec(i))*(catalan_rec(n-1-i))
    return b

print(catalan_rec(5))




