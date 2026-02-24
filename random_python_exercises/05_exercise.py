def binary_gap(n: int):
    binary_array = []
    number_copy = n
    adjacent = 0

    while number_copy > 0:
        binary_array.append(number_copy % 2)
        number_copy = number_copy // 2

    binary_array.reverse()
    print(list(binary_array))

    counter_zeros = 0
    for index, value in enumerate(binary_array):
        if value == 0:
            counter_zeros += 1
        if index > 0:
            if binary_array[index-1] == 0 and value == 1:
                if adjacent <= counter_zeros:
                    adjacent = counter_zeros + 1
                counter_zeros = 0
            if binary_array[index-1] == 1 and value == 1 and adjacent < 1:
                adjacent = 1
    
    return adjacent


input_one, input_two, input_three, input_four, input_five = 5, 6, 8, 9, 22
print(binary_gap(input_one))
print(binary_gap(input_two))
print(binary_gap(input_three))
print(binary_gap(input_four))
print(binary_gap(input_five))