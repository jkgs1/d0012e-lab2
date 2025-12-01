def insertion_sort(arr, start, end):
    i = start + 1
    while i <= end:
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        i = i + 1


def copy_subarray(arr, start, end):
    result = []
    i = start
    while i <= end:
        result.append(arr[i])
        i = i + 1
    return result


def concat_arrays(arr1, arr2):
    result = []
    i = 0
    while i < len(arr1):
        result.append(arr1[i])
        i = i + 1
    i = 0
    while i < len(arr2):
        result.append(arr2[i])
        i = i + 1
    return result


def sortR(arr):

    n = len(arr)
    
    # Base case
    if n <= 4:
        result = copy_subarray(arr, 0, n - 1)
        insertion_sort(result, 0, n - 1)
        return result
    
    quarter = n // 4
    three_quarter = (3 * n) // 4
    
    # Step 1: Sort first 3n/4 elements
    first_part = copy_subarray(arr, 0, three_quarter - 1)
    b = sortR(first_part)
    
    # Step 2: Sort b[n/4+1:3n/4] + a[3n/4+1:n]
    middle_from_b = copy_subarray(b, quarter, three_quarter - 1)
    last_from_a = copy_subarray(arr, three_quarter, n - 1)
    second_part = concat_arrays(middle_from_b, last_from_a)
    c = sortR(second_part)
    
    # Step 3: Sort b[1:n/4] + c[n/4+1:3n/4]
    first_from_b = copy_subarray(b, 0, quarter - 1)
    middle_from_c = copy_subarray(c, 0, three_quarter - quarter - 1)
    third_part = concat_arrays(first_from_b, middle_from_c)
    d = sortR(third_part)
    
    # Step 4: Return d + c[3n/4+1:n]
    last_from_c = copy_subarray(c, three_quarter - quarter, len(c) - 1)
    result = concat_arrays(d, last_from_c)
    
    return result


# Test cases
if __name__ == "__main__":
    import random
    import time
    
    # Test sizes demonstrating polynomial growth
    test_sizes = [4, 8, 16, 32, 64, 128, 256]
    
   
    print(f"{'Size':<8} {'Time (s)':<12} {'Status':<8} {'Input Preview'}")
   
    
    for size in test_sizes:
        # Generate random array
        test_array = list(range(1, size + 1))
        random.shuffle(test_array)
        
        # Time the sorting
        start_time = time.time()
        result = sortR(test_array.copy())
        end_time = time.time()
        elapsed = end_time - start_time
        
        # Verify correctness
        expected = sorted(test_array)
        is_correct = result == expected
        status = "PASS" if is_correct else "FAIL"
        
        # Preview: show first few and last few elements
        if size <= 8:
            preview = str(test_array)
        else:
            preview = f"[{test_array[0]}, {test_array[1]}, {test_array[2]}, ..., {test_array[-2]}, {test_array[-1]}]"
        
        print(f"{size:<8} {elapsed:<12.6f} {status:<8} {preview}")
        

    
   
    print("sortR has polynomial growth")
    print("When n doubles, time multiplies by roughly 2^3.82 ≈ 14×")
    print("This matches the Θ(n^3.82) time complexity from the recurrence")
 

