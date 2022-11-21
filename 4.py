def matrix(arr) :
    firstzero = [-1,-1]
    lastzero = [-1,-1]

    for i in range(256) :
        for j in range(256) :
            if arr[i][j] == 0 and firstzero[0] == -1 :
                firstzero[0] = i
                firstzero[1] = j
                lastzero[0] = i
                lastzero[1] = j
            if arr[i][j] == 0 :
                if lastzero[0] < i :
                    lastzero[0] = i
                if lastzero[1] < j :
                    lastzero[1] = j
    return [tuple(firstzero),(firstzero[0],lastzero[1]), (lastzero[0],firstzero[1]) , tuple(lastzero)]

arr = []
for i in range(256) :
    l = []
    for j in range(256) :
        l.append(int(input()))
    arr.append(l)

print(*matrix(arr))