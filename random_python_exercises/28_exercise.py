from typing import List

# with Bubble Sort algorithm
def sortColors(nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            swapped: bool = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break

# with Dutch National Flag algorithm
def sortColors(nums: List[int]) -> None:
        low: int = 0
        mid: int = 0
        high: int = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# with Quick Sort algorithm
def sort_colors(nums: list[int]) -> None:
     nums = quick_sort(nums)
     print(nums)

def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers

    pivot: int = numbers[0]
    lower: list[int] = []
    higher: list[int] = []

    for i in range(1, len(numbers)):
        value: int = numbers[i]

        if value <= pivot:
            lower.append(value)
        else:
            higher.append(value)

    return quick_sort(lower) + [pivot] + quick_sort(higher)

sort_colors([14,56,78,26,33,7,85])
     