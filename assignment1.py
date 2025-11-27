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
    test2 = array_sorter(a)

# ===========================================
#               For O(n³)-time
# ===========================================
def worst_case_three(arr: array, i, j, k):
    length = len(arr)

    # If i hits the end there is no solution
    if i >= length:
        print("Nah 3x")
        return False

    # If j hits the end we move to the next i
    if j >= length:
        return worst_case_three(arr, i+1, i+1, 0)

    # If k hits the end we move to the next j
    if k >= length:
        return worst_case_three(arr, i, j+1, 0)

    if i != j and i != k and j != k:
        if arr[i] + arr[j] == arr[k]:
            print(arr[i], "+", arr[j], "=", arr[k])
            return True

    # If none of the if statements is matched,
    # continue the recursion with the next k
    return worst_case_three(arr, i, j, k+1)

# ===========================================
#               For O(n²)-time
# ===========================================
def array_sorter(arr: array):
    # Sorting the array, O(n*log(n))
    sorted_array = sorted(arr)
    return firstloop(sorted_array, 2)

def firstloop(arr: array, k):
    length = len(arr)

    # Since the array is sorted, we always set i=0 and j=z-1
    # because neither i nor j can have a higher position in the array than k
    if k >= length:
        print("Nah 2x")
        return False
    elif secondloop(arr, 0, k-1, k):
        return True

def secondloop(arr: array, i, j, k):

    if i >= j:
        return firstloop(arr, k+1)

    # k is the target here, if i+j is smaller than k we
    # need to increase i, if they are larger than k we need
    # to decrease j instead. Loop this until i and j collide
    if arr[i]+arr[j] == arr[k]:
        print(arr[i], "+", arr[j], "=", arr[k])
        return True
    elif arr[i]+arr[j] < arr[k]:
        return secondloop(arr, i+1, j, k)
    elif arr[i]+arr[j] > arr[k]:
        return secondloop(arr, i, j-1, k)





main()
