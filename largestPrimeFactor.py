def findLargePrime(number):
    index=2
    while index*index<number:
        if number%index:
            index=index+1
        else:
            number=number/index
    return number
print(int(findLargePrime(13195)))