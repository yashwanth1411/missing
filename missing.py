def find_repeating_and_missing(nums):
    n = len(nums)
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
        xor_all ^= nums[i - 1]

    # Find the rightmost set bit in xor_all
    rightmost_set_bit = xor_all & -xor_all

    # Initialize variables to track xor for missing and repeating numbers
    xor_missing = 0
    xor_repeating = 0

    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            xor_missing ^= i
        else:
            xor_repeating ^= i

        if nums[i - 1] & rightmost_set_bit:
            xor_missing ^= nums[i - 1]
        else:
            xor_repeating ^= nums[i - 1]

    # Check which one is actually missing
    for num in nums:
        if num == xor_missing:
            return [xor_repeating, xor_missing]

    return [xor_missing, xor_repeating]


input_array = []
a = int(input())
for i in range(a):
    j = int(input())
    input_array.append(j)
output_result = find_repeating_and_missing(input_array)
print(output_result)
