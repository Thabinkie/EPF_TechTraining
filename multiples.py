sum=0
index=999

while index>0:
    num1=index%3
    num2=index%5
    
    if num1==0 or num2==0:
        print(index)
        sum=sum+index
    index=index-1
print(sum)
