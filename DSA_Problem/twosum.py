#------------------finding whether sum of a pair in an array is equal to target given... --------------------
# Function to check whether any pair exists
# whose sum is equal to the given target value
def twoSum(arr, target):
    n = len(arr)

    # Iterate through each element in the array
    for i in range(n):
      
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
          
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                return True
              
    # If no pair is found after checking
    # all possibilities
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    if twoSum(arr, target):
        print("true")
    else:
        print("false")

#----------------------finding number of 1's in a boolian number-----------------------------------

# Function to get no of set bits in binary
# representation of passed binary no. */
i = int(input())
def countSetBits(n):

    count = 0
    while (n):
        n &= (n-1) 
        count+= 1
    
    return count


# Program to test function countSetBits 

print(countSetBits(i))
 
#