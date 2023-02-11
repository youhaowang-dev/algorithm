# https://leetcode.com/problems/basic-calculator
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "1 + 1"
# Output: 2
# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# 1+(2-(3+4))-5
#  0  1  2   0
# 1  2  3 4   5 => 3+4, 2-7, 1+-5, -4-5 => 9
# get the priority of each operator
class BasicCalculator:
    def calculate(self, s: str) -> int:
        # pre-processing to tokenize input
        s = s.replace(" ", "")  # remote white space

        tokens = []  # collect tokens
        left = right = 0
        while right <= len(s):
            if right == len(s) or s[right] in "+-()":
                if left < right:
                    tokens.append(s[left:right])
                if right < len(s):
                    tokens.append(s[right])
                left = right + 1
            right += 1

        operator_level = 0
        operator_stack = deque()
        number_stack = deque()
        for token in tokens:
            if token.isdigit():
                number_stack.append(int(token))
            elif token == "(":
                operator_level += 1
            elif token == ")":
                operator_level -= 1
            elif token in "+-":
                while operator_stack and operator_stack[-1][1] >= operator_level:
                    self.merge(operator_stack, number_stack)
                operator_stack.append((token, operator_level))
            else:
                pass

        while operator_stack:
            self.merge(operator_stack, number_stack)

        return number_stack[-1]

    def merge(self, operator_stack, number_stack):
        number = number_stack.pop()
        prev_number = number_stack.pop()
        operator, _ = operator_stack.pop()
        if operator == '+':
            number_stack.append(prev_number + number)
        if operator == "-":
            number_stack.append(prev_number - number)
