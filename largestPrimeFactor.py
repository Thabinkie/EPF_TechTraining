def largestPrimeFactor(n):
    
    i=2
    while i*i <=n:
        if n % i == 0:
           
            n//=i
        else:
            i=i+1
    
    return n
print(largestPrimeFactor(600851475143))
