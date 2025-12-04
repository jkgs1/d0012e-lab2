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
def worst_case_two(arr, x=None, y=None, z=None, l=None, r=None):

    n = len(arr)

    # -----------------------------------------------
    # initial iteration to start sorting
    # -----------------------------------------------

    if x is None and y is None and z is None and l is None and r is None:
        if n < 3:
            print("No solution found")
            return False
        # start with sorting
        return worst_case_two(arr, l=0, r=n-1)

    # -----------------------------------------------
    # sorting phase (presence of l/r signals sorting)
    # -----------------------------------------------

    if l is not None and r is not None:
        # base case
        if l >= r:
            return True
        # divide
        m = (l + r) // 2
        worst_case_two(arr, l=l, r=m)
        worst_case_two(arr, l=m+1, r=r)
        # merge
        i, j = l, m + 1
        tmp = array("i")
        # merge two sorted halves
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                tmp.append(arr[i]); i += 1
            else:
                tmp.append(arr[j]); j += 1
        # append remaining elements
        while i <= m:
            tmp.append(arr[i]); i += 1
        while j <= r:
            tmp.append(arr[j]); j += 1
        arr[l:r+1] = tmp # copy back to original array
        # after the top-level merge, start search
        if l == 0 and r == n - 1:
            return worst_case_two(arr, x=0, y=1, z=2)
        return True

    # -----------------------------------------------
    # searching phase using two-pointer
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
