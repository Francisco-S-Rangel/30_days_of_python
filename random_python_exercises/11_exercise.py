def remove_duplicates(nums: list[int]) -> int:
    length: int = 0

    for index, value in enumerate(nums):
        if  index == 0 or value != nums[index -1]:
            nums[length] = value
            length += 1
    
    return length

print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))