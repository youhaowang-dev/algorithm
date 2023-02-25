# Array, String, Simulation
# Google 10 Capital One 5 Karat 4 LinkedIn 3 Uber 3 Airbnb 3 Apple 2 Twitter 2 Twilio 2 Facebook 6 Coursera 5
# Microsoft 4 Roblox 4 Indeed 3 Amazon 2 Twitch 2 Bloomberg 2 GoDaddy 2 Intuit 24 Reddit 11 Square 5 eBay 4
# TikTok 4 Databricks 3 Netflix 3 Coinbase 3 Oracle 2 Quora 2 Nvidia 2 PhonePe 2 Wayfair 2
# https://leetcode.com/problems/text-justification/

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly
# maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
# divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

from ast import List

# TODO: 虽然不太可能考，但还是搞熟练
# https://www.lintcode.com/problem/1361/solution/58613
class TextJustification:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        ans = list()
        right, n = 0, len(words)
        while True:
            left = right  # 当前行的第一个单词在 words 的位置
            line_word_total_length = 0  # 统计这一行单词长度之和
            # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
            while (
                right < n
                and line_word_total_length + len(words[right]) + right - left
                <= max_width
            ):
                line_word_total_length += len(words[right])
                right += 1

            # 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + self.get_spaces(max_width - len(s)))
                break

            num_words = right - left
            num_spaces = max_width - line_word_total_length

            # 当前行只有一个单词：该单词左对齐，在行末填充空格
            if num_words == 1:
                ans.append(words[left] + self.get_spaces(num_spaces))
                continue

            # 当前行不只一个单词
            avg_spaces = num_spaces // (num_words - 1)
            extra_spaces = num_spaces % (num_words - 1)
            s1 = self.get_spaces(avg_spaces + 1).join(
                words[left : left + extra_spaces + 1]
            )  # 拼接额外加一个空格的单词
            s2 = self.get_spaces(avg_spaces).join(
                words[left + extra_spaces + 1 : right]
            )  # 拼接其余单词
            ans.append(s1 + self.get_spaces(avg_spaces) + s2)

        return ans

    def get_spaces(self, n: int) -> str:
        return " " * n
