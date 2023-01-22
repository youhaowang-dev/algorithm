# String
# Amazon 4 Apple 2 Yahoo 2 Zopsmart 2 Adobe 4 Google 2 Facebook 2 Paypal 2 Zoho 2 Bloomberg 6 Uber 3 Microsoft 3 Oracle 2
# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Simulate Zig-Zag Movement, row index goes down and up
# abcdef => aebdfc
# a   e
# b d f
# c
class ZigzagConversion:
    def convert(self, s: str, row_count: int) -> str:
        if row_count == 1:
            return s

        rows = ["" for _ in range(row_count)]
        row_index = 0
        go_down = True  # index += 1

        for character in s:
            rows[row_index] += character
            if row_index + 1 == row_count:
                go_down = False
            elif row_index == 0:
                go_down = True

            if go_down:
                row_index += 1
            else:
                row_index -= 1

        return "".join(rows)
