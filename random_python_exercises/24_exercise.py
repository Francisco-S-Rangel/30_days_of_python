from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set_intersection: set[int] = set()
    array_one: List[int] = sorted(nums1)
    array_two: List[int] = sorted(nums2)

    for item_array_one in array_one:
        low: int = 0
        high: int = len(array_two) - 1

        while low <= high:
            mid_position: int = (low + high) // 2
            item_array_two: int = array_two[mid_position]

            if item_array_two == item_array_one:
                set_intersection.add(item_array_two)
                break
            elif item_array_two > item_array_one:
                high = mid_position - 1
            else:
                low = mid_position + 1

    return list(set_intersection)

# def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
#     return list(set(nums1) & set(nums2))

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))