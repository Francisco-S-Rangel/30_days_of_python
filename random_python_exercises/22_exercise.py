from typing import List

def map_word_weights(words: List [str], weights: List[int]) -> str:
    mapped_string: str = ""
    all_letters: str = "abcdefghijklmnopqrstuvwxyz"
    letters_map: dict[str, int] = {}
    reverse_map: dict[int, str] = {}

    weight_reverse: int = 25
    for index, value in enumerate(all_letters):
        letters_map[value] = weights[index]
        reverse_map[weight_reverse] = value
        weight_reverse = weight_reverse - 1

    for word in words:
        length_word: int = len(word)
        sum: int = 0
        for index in range(length_word):
            sum = sum + letters_map.get(word[index])
        mapped_string = mapped_string + reverse_map[sum % 26]

    return mapped_string

words: List[str] = ["abcd","def","xyz"]
weights: List[int] = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

print(map_word_weights(words, weights))