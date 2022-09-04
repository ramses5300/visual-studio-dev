# Python3 Naive program to
# shuffle an array of size 2n
 
# Function to shuffle an array of size 2n
def shuffleArray(a, n):
 
    # Rotate the element to the left
    i, q, k = 0, 1, n
    while(i < n):    
        j = k
        while(j > i + q):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
        k += 1
        q += 1
 
# Driver Code
a = [1, 3, 5, 7, 2, 4, 6, 8]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n):
    print(a[i], end = " ")
 
# This code is contributed by Smitha Dinesh Semwal.
