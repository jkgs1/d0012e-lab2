from typing import List

class Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:

        def build(l: int, r: int):
            # Base case: interval of length 1
            if r - l == 1:
                val = nums[l]
                return (val, val, val, val)   # total, prefix, suffix, best

            # Divide the interval into two halves
            mid = (l + r) // 2
            left  = build(l, mid)   # results for left half
            right = build(mid, r)   # results for right half

            # Combine results from left and right
            return merge(left, right)

        def merge(left, right):
            # 1. Total sum of both halves
            total_sum = left[0] + right[0]

            # 2. Best prefix: either left prefix or whole left + right prefix
            max_prefix = max(left[1], left[0] + right[1])

            # 3. Best suffix: either right suffix or right total + left suffix
            max_suffix = max(right[2], right[0] + left[2])

            # 4. Best subarray: left best, right best, or crossing
            max_sub = max(left[3], right[3], left[2] + right[1])

            return (total_sum, max_prefix, max_suffix, max_sub)

        # Only the "best subarray" value (index 3) is the desired answer.
        return build(0, len(nums))[3]

# Example usage
nums = [2, -1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(nums))
