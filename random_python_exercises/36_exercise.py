def longest_common_prefix(strs: list[str]) -> str:
    common_prefix: str = ""
    str_compare: str = strs[0]

    for i in range(1, len(strs)):
        current_str: str = strs[i]

        for z in range(min(len(current_str), len(str_compare))):
            if current_str[z] != str_compare[z]:
                break

            common_prefix = common_prefix + current_str[z]

        str_compare = common_prefix
        common_prefix = ""

    common_prefix = str_compare
    return common_prefix

print(longest_common_prefix(["flower","flow","flight"]))