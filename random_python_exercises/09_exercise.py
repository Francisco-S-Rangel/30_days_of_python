import re
def is_palindrome(s: str) -> bool:
    return re.sub(r"[^a-zA-Z0-9]","",s).lower() == "".join(reversed(re.sub(r"[^a-zA-Z0-9]","",s))).lower()

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))
