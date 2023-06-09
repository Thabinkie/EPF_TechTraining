def sum_even_fibonacci(limit):
  num1=1
  num2=1
  num3=0
  sum=0 

  while num3<limit:
      #Next value in a fibonacci sequence is the sum of the two previous values
        num3=num1+num2
        
        num1=num2
        num2=num3
      #Test if the next value is an even number or not  
        if  num3 % 2 == 0:    
            sum=sum+num3
  return sum

print(sum_even_fibonacci(4000000))