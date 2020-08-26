def sum(nums):
    res = 0
    for num in nums:
        if isinstance(num, list):
            res += sum(num)
        else:
            res += num

    return res

numbers = [
    [1, 2, 3, 4],

    [3, 6, [5, 6], 8, 2,[2, 4], 9],

    [4, 2, [6, 7, [2, 6, 1]]]
]


print(sum(numbers))
