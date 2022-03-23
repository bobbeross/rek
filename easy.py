
def arrow(n):
    # for x in range(int(n/2)):
    #     string_1 = '  '+'@'*(n-4)+'  '
    #     print(string_1)
    for y in range(int(n/2)):
        string_2 = ' '*(y-1) +'@'*int((n-y-1)/2)+'@'*int((n-y-1)/2)+' '*(y-1)
        print(string_2)




arrow(10)



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
