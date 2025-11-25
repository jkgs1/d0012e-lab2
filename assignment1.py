from array import array
import random

def main():
    n=10
    min_val, max_val = 0, 100
    a = array("i", random.sample(range(min_val,max_val),n))
    test = worst_case_three(a)

def worst_case_three(arr: array):
    count = 0
    length = len(arr)


def notRecursive(arr: array):
    for i in range(len(arr)):
        x = arr[i]
        for j in range(i+1, len(arr)):
            y = arr[j]
            for k in range(len(arr)):
                if k!=i and k!= j:
                    z = arr[k]
                    if x + y == z:
                        print(x, y, z)
                        return True
    print("nah")
    return False

main()
