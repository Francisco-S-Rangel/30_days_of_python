def permute(nums: list[int]) -> list[list[int]]:
    permuted_array: list[list[int]] = []

    def permutation(k: int, array: list[int]) -> None:
        if k == 1:
            permuted_array.append(array.copy())
        else:
            for i in range(k - 1):
                permutation(k - 1, array)

                if k % 2 == 0:
                    array[i], array[k - 1] = array[k -1], array[i]
                else:
                    array[0], array[k - 1] = array[k - 1], array[0]

        
            permutation(k - 1, array)

    permutation(len(nums), nums.copy())
    return permuted_array       

print(permute([1, 2, 3]))
print(permute([0,1]))
print(permute([1]))                        