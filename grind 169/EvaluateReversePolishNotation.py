# Array, Math, Stack
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# do as the requirement asks for, time n space n where all operators put at the end
# put numbers in stack, for operator, take out two number and get the result and put back
class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        # assume input is valid
        stack = deque()
        for token in tokens:
            if token not in "+-*/":  # isnumeric wont work for negative string number
                stack.append(int(token))
            else:
                stack.append(self.get_result(stack, token))

        return stack.pop()

    def get_result(self, stack, operator):
        second = stack.pop()
        first = stack.pop()
        if operator == "+":
            return first+second
        elif operator == "-":
            return first-second
        elif operator == "*":
            return first*second
        elif operator == "/":
            if first * second >= 0:
                return first // second
            else:
                return -(abs(first) // abs(second))
        else:
            raise Exception('invalid operator')
