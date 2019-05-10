#function to return gcd of a and b
def gcd(m,n):
    #Everything divides 0
    if n==0:
        return m 
    i = min(m,n)
    while i>0:
        if m%i==0 and n%i==0:
            return i
        else:
            i -=1
#Main Program
print(gcd(int(input("Enter number 1 ")),int(input("Enter number 2 "))))

#Output
#Enter number 1 14
#Enter number 2 63
#7
