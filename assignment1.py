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
    test = worst_case_three(a,0,0,0)
    test2 = worst_case_two(a, None, None, None, None, None)
# ===========================================
#               For O(n³)-time
# ===========================================
def worst_case_three(arr: array, x, y, z):
    length = len(arr)

    if x >= length:
        print("No solution found")
        return False

    if y >= length:
        return worst_case_three(arr, x+1, x+1, 0)

    if z >= length:
        return worst_case_three(arr, x, y+1, 0)

    if z != y and z != x and y != x:
        if arr[x] + arr[y] == arr[z]:
            print(arr[x], "+", arr[y], "=", arr[z])
            return True

    return worst_case_three(arr, x, y, z+1)

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
        return worst_case_two(arr, x=0, y=z-1, z=z + 1)

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
