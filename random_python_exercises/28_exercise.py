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