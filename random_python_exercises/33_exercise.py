def find_missing_elements(nums: list[int]) -> list[int]:
    sorted_nums: list[int] = sorted(nums)
    aux: int = 0
    missing_elements: list[int] = []

    for i in range(sorted_nums[0], sorted_nums[len(sorted_nums) - 1] + 1):
        if sorted_nums[aux] != i:
            missing_elements.append(i)
        else:
            aux += 1

    return missing_elements

print(find_missing_elements([1,4,2,5]))
print(find_missing_elements([7,8,6,9]))
print(find_missing_elements([5,1]))