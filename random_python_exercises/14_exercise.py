def remove_element(nums: list[int], val: int) -> int:
    length: int = 0

    for index, value in enumerate(nums):
        if value != val:
            nums[length] = nums[index]
            length += 1
    
    return length

print(remove_element([3,2,2,3], 3))
print(remove_element([0,1,2,2,3,0,4,2], 2))