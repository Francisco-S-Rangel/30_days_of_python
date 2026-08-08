def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    pivot: int = nums[0]
    lower: list[int] = [i for i in nums[1:] if i <= pivot]
    higher: list[int] = [i for i in nums[1:] if i > pivot]

    return quick_sort(lower) + [pivot] + quick_sort(higher)

print(quick_sort([14,85,2,69,77,45,13,5,8,97,33])),

def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    pivot: int = nums[0]
    lower: list[int] = []
    higher: list[int] = []

    for i in range(1, len(nums)):
        value: int = nums[i]

        if value <= pivot:
            lower.append(value)
        else:
            higher.append(value)

    return quick_sort(lower) + [pivot] + quick_sort(higher)

print(quick_sort([14,85,2,69,77,45,13,5,8,97,33])),

