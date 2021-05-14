#Eg. If you input 11, you will get [3,1,0] because, 2^3 + 2^1 + 2^0 = 11
def powers_of_2(n):
    power_lst = []
    x = bin(n)[2:][::-1]
    for i in range(0,len(x)):
        if x[i] == '1':
            power_lst.append(i)
    return power_lst[::-1]


# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(n**0.5+1),2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n) 
