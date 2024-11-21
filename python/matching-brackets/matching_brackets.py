def is_paired(input_string: str) -> bool:
    stack = []

    # Iterating through each character in the given string
    for char in input_string:
        # If it's an opening bracket, brace or parentheses push it onto the stack
        if char in '([{':
            stack.append(char)
        # If it's a closing bracket, check if it matches the top of the stack
        elif char in ')]}':
            if not stack:
                return False  # If stack is empty, it means no opening bracket for this closing one
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == ']' and top != '[':
                return False
            if char == '}' and top != '{':
                return False

    # If the stack is empty, it means all brackets are matched and closed properly
    return not stack
