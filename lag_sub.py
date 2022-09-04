# python program to find size of the
# largest subset with GCD 1
 
# Function to return gcd of a and b
def gcd( a, b):
     
    if (a == 0):
        return b
         
    return gcd(b%a, a)
 
 
# Function to find largest subset
# with GCD 1
def largestGCD1Subset(A, n):
     
    # finding gcd of whole array
    currentGCD = A[0];
    for i in range(1, n):
         
        currentGCD = gcd(currentGCD, A[i])
 
        # If current GCD becomes 1 at
        # any moment, then whole
        # array has GCD 1.
        if (currentGCD == 1):
            return n
    return 0
 
# Driver code
A = [2, 18, 6, 3]
n = len(A)
print (largestGCD1Subset(A, n))
 
# This code is Contributed by Sam007.
