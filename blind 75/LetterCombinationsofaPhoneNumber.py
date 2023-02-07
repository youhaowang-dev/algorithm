# Hash Table, String, Backtracking
# Amazon 27 Microsoft 4 Facebook 4 Uber 4 Google 3 Apple 3 eBay 2 Bloomberg 2 Adobe 4 Oracle 4 VMware 3 Twilio 3
# Walmart Global Tech 2 Twitch 2 Swiggy 2 DE Shaw 2 Epic Systems 6 Twitter 5 Intuit 5 Cisco 5 Goldman Sachs 5
# Tesla 4 Duolingo 4 Morgan Stanley 3 Nutanix 3 Snapchat 2 Square 2 LinkedIn 2 Samsung 2 JPMorgan 2 ServiceNow 2 Capital One 2 Dropbox
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


from ast import List
from collections import deque


# "23"
# [''] => ['a', 'b', 'c'] => ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
class LetterCombinationsofaPhoneNumber:
    DIGIT_TO_LETTERS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        results = list()
        if not digits:
            return results

        results.append("")
        for digit in digits:
            results = self.update_results(results, digit)

        return results

    def update_results(self, results: List[int], digit: str):
        new_results = list()
        letters = self.DIGIT_TO_LETTERS.get(digit)
        for result in results:
            for letter in letters:
                new_results.append(result + letter)

        return new_results
