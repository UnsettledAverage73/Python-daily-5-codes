"""
Day 28: Check for Balanced Parentheses using Stack

✅ Input: string with (), {}, []
✅ Output: True if balanced, False otherwise

🧠 Idea:
- Push opening brackets to stack
- For every closing bracket, check if it matches the last opening
"""

def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack  # If stack is empty, it's balanced


# ✅ Test cases
if __name__ == "__main__":
    tests = [
        ("(a+b)", True),
        ("{[()]}", True),
        ("(a+b]", False),
        ("(((())))", True),
        ("[{])}", False),
        ("", True),
    ]

    for expr, expected in tests:
        result = is_balanced(expr)
        print(f"🔎 Expression: {expr} → {'✅ Balanced' if result else '❌ Not Balanced'} (Expected: {expected})")
