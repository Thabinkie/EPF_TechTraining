var=1000
num=1
sum=0

while (num<var):
    if num % 3 == 0 or num % 5 == 0:
        sum= sum + num
    num=num+1
    
print(sum)
