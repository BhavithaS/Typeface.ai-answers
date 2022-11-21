def occurrences(str1,str2) :
    last_chr = str2[-1]
    count = 0
    for i in str1 :
        if i == last_chr :
            count += 1
    return count

str1 = input(' Enter the first string ')
str2 = input(' Enter the second string ')

print(occurrences(str1,str2))