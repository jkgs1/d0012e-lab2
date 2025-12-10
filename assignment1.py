from array import array
import random

def main():
    n=10
    min_val, max_val = 0, 100
    a = array("i", random.sample(range(min_val,max_val),n))
    b = sorted(a)
    for i in range(len(b)):
        #print(b[i])
        print(a[i])
    test = findXYZ(a,0,0,None)
    test2 = worst_case_two(a, None, None, None, None, False)
# ===========================================
#               For O(n³)-time
# ===========================================
def findXYZ(arr: array, z, i, hashmap):

    if z >= len(arr):
        print("No solution found")
        return False

    # Init hashmap on every z iteration
    if hashmap is None:
        hashmap = {}

    if i < len(arr):
        complement = arr[z] - arr[i]
        # Check if the compliment has been computed/ stored in a previous iteration
        # Also check for x + 0 = x
        if complement in hashmap and hashmap[complement] != i and hashmap[complement] != z:
            print(complement, "+", arr[i], "=", arr[z])
            return True
        # If not, store current value for future iterations and recursively call function
        # for every value i to the length of the array
        hashmap[arr[i]] = i
        return findXYZ(arr, z, i + 1, hashmap)
    # When every value for i has been checked, call function again with next z-value
    return findXYZ(arr, z+1, 0, None)

# ===========================================
#               For O(n²)-time
# ===========================================
def worst_case_two(arr, x=None, y=None, z=None, l=None, r=False):

    n = len(arr)

    # -----------------------------------------------
    # initial iteration to start sorting
    # -----------------------------------------------

    if x is None and y is None and z is None and l is None and not r:
        if n < 3:
            print("No solution found")
            return False
        # start with sorting
        return worst_case_two(arr, l=1, r=True)

    # -----------------------------------------------
    # sorting phase, incremental recursive insertion sort
    # -----------------------------------------------

    if r:
        # base case: if l goes out of bounds, start searching phase
        if l >= n:
            return worst_case_two(arr, x=0, y=None, z=None, l=None, r=False)
        # inner loop: insertion sort step
        key = arr[l]
        j = l - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # recursive call to sort next element
        return worst_case_two(arr, l=l + 1, r=True)

    # -----------------------------------------------
    # searching phase using two-pointer method
    # -----------------------------------------------

    # init z, y
    if z is None:
        z = 2
    if y is None:
        y = z - 1
    # base case: if z goes out of bounds, no solution
    if z >= n:
        print("No solution found")
        return False
    # reset x, check y
    if x is None:
        x = 0
    if x >= y:
        # move to next z
        return worst_case_two(arr, x=0, y=z, z=z + 1)

    target = arr[x] + arr[y]
    # either find match
    if target == arr[z]:
        print(arr[x], "+", arr[y], "=", arr[z])
        return True
    # or if target is smaller than z, move pointer x up
    if target < arr[z]:
        return worst_case_two(arr, x + 1, y, z)
    # or if target is bigger than z, move pointer y down
    return worst_case_two(arr, x, y - 1, z)





main()
