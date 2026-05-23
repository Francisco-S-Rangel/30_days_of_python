def transpose(matrix: list[list[int]]) -> list[list[int]]:
    newMatrix: list[list[int]] = []
    column: int = 0

    for index, value in enumerate(matrix[0]):
        newArray: list[int] = []
        for index_2, value_2 in enumerate(matrix):
            newArray.append(matrix[index_2][column])
        newMatrix.insert(index, newArray)
        column += 1

    return newMatrix

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[5],[8]]))
print(transpose([[-51,36,-31,23],[3,12,-31,65],[-20,2,-42,-62],[0,-49,75,77],[-52,46,45,37],[-98,17,14,78],[50,88,-15,-31],[84,-59,-96,23],[42,1,48,81],[-92,95,-71,37]]))