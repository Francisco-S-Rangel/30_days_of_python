def search_insert(nums: list[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) -1

    while (left <= right):
        center: int = left + ((right - left) // 2)

        if nums[center] == target:
            return center
        elif nums[center] < target:
            left = center + 1
        else:
            right = center - 1

    return left

print(search_insert([1,3,5,6], 5))
print(search_insert([1,3,5,6], 2))
print(search_insert([1,3,5,6], 7))
print(search_insert([1,3], 2))