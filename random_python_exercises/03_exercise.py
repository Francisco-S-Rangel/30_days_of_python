# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

numbers = [2,7,11,15]
target = 9

def sum_numbers_target(numbers, target):
    for index, number in enumerate(numbers):
        for index_two, number_two in enumerate(numbers):
            if number + number_two == target and index != index_two:
                return [index, index_two]

print(sum_numbers_target(numbers, target))

print("---------------------")

def sum_numbers_target_dict(numbers, target):
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        
        seen[number] = index

print(sum_numbers_target_dict(numbers, target))
