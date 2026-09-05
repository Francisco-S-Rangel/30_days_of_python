def is_valid(s: str) -> bool:
    order_stack: list[str] = []

    for char in s:
        if char == ")":
            if not order_stack or order_stack.pop() != "(":
                return False
        elif char == "]":
            if not order_stack or order_stack.pop() != "[":
                return False
        elif char == "}":
            if not order_stack or order_stack.pop() != "{":
                return False
        else:
            order_stack.append(char)