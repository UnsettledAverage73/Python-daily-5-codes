"""
Day 30: Evaluate Postfix Expression

✅ Input: Postfix expression (e.g., 3 4 + 5 *)
✅ Output: Result (e.g., 35)

💡 Works only with numbers (not variables like A, B)
"""

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # operand
            stack.append(int(token))
        else:
            # operator: pop two operands
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))  # force int for consistency

    return stack[0] if stack else None


# ✅ Test cases
if __name__ == "__main__":
    expressions = [
        "3 4 +",         # 3 + 4 = 7
        "3 4 + 5 *",     # (3 + 4) * 5 = 35
        "6 2 / 3 -",     # (6 / 2) - 3 = 0
        "5 1 2 + 4 * + 3 -", # 5 + ((1+2)*4) - 3 = 14
    ]

    for expr in expressions:
        result = evaluate_postfix(expr)
        print(f"🧮 Postfix: {expr} → Result: {result}")

