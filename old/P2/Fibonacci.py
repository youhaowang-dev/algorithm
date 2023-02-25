# https://www.lintcode.com/problem/366/
class Fibonacci:
    def fibonacci(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1

        prev_prev = 0
        prev = 1
        result = 0
        for _ in range(3, n + 1):
            result = prev_prev + prev
            prev_prev = prev
            prev = result

        return result
