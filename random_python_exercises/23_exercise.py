def lengthOfLastWord(s: str) -> int:
    length_last_word: int = 0

    for i in range(len(s) - 1, -1, -1):
        if length_last_word != 0 and s[i] == " ":
            break

        if s[i] != " ":
            length_last_word += 1

    return length_last_word

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))