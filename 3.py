def LCD_series(n) :
    good_num = {0,1,2,5,6,8,9}
    i = 0
    j = 1
    while i!= n :
        s = set(list(map(int,str(j))))
        if s.issubset(good_num) :
            i += 1
        j += 1
    return j-1

n = int(input())
print(LCD_series(n))