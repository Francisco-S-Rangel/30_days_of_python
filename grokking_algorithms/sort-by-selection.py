from typing import List

def get_smallest_number(arr: List[int]) -> int:
    smallest_number: int = arr[0]
    lowest_index: int = 0

    for index in range(1, len(arr)):
        if arr[index] < smallest_number:
            smallest_number = arr[index]
            lowest_index =  index
    
    return lowest_index

def sort_by_selection(arr: List[int]) -> List[int]:
    sorted_arr: List[int] = []

    for index in range(len(arr)):
        smallest: int = get_smallest_number(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr

print(sort_by_selection([5, 3, 6, 2, 10]))