#converting from Denary to Binary
def DenToBin(n):
    result = ''
    while n != 0:
        current = n%2
        result+=str(current)
        n = n//2
    bin_n = result[::-1]
    return bin_n

#Converting from Binary to Denary
def bin2den(binary): 
    den, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        den = den + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return den     
