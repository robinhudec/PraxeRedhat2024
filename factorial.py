def fact(value):
    n = 1
    result = 0
    for i in range (value):
        result = (i+1) * n
        n +=1
    return(result)

print(fact(5))
