def base3(n) :
    sign = '-' if n < 0 else ''
    n = abs(n)
    if n < 3 :
        return str(n)
    res = ''
    while n!= 0 :
        res = str(n%3) + res
        n = n//3
    return sign + res

n = int(input())
print(base3(n))