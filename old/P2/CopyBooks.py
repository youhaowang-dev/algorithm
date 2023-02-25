# https://www.lintcode.com/problem/437/description
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

# These books list in a row and each person can claim a continous range of books. For example,
# one copier can copy the books from i-th to j-th continously, but he can not copy the
# 1st book, 2nd book and 4th book (without 3rd book).

# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?

# Return the shortest time that the slowest copier spends.

# Example 1:
# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation:
#     First person spends 5 minutes to copy book 1 and book 2.
#     Second person spends 4 minutes to copy book 3.

# Example 2:
# Input: pages = [3, 2, 4], k = 3
# Output: 4
# Explanation: Each person copies one of the books.

from math import ceil
from typing import List

# search a min allowed copy time per person
class CopyBooks:
    def copy_books(self, pages: List[int], max_person: int):
        if not pages:
            return 0

        # each person copies one book, slowest bounds the time
        min_page_per_person = max(pages)
        # one person copies all books
        max_page_per_person = sum(pages)

        while min_page_per_person + 1 < max_page_per_person:
            person_needed = self.get_person_needed(pages, min_page_per_person)
            if person_needed > max_person:
                min_page_per_person += 1
            if person_needed < max_person:
                return min_page_per_person
            if person_needed == max_person:
                return min_page_per_person

        if self.get_person_needed(pages, min_page_per_person) <= max_person:
            return min_page_per_person
        if self.get_person_needed(pages, max_page_per_person) <= max_person:
            return max_page_per_person

        return max_page_per_person

    def get_person_needed(self, pages: List[int], time_per_person) -> int:
        person_needed = 1  # at least one person copy all books
        page_sum = 0
        for page in pages:
            page_sum += page
            if page_sum > time_per_person:  # need another person
                page_sum = page
                person_needed += 1

        return person_needed


# binary search
class CopyBooks2:
    def copy_books(self, pages: List[int], max_person: int):
        if not pages:
            return 0

        # each person copies one book, slowest bounds the time
        min_page_per_person = max(pages)
        # one person copies all books
        max_page_per_person = sum(pages)
        while min_page_per_person + 1 < max_page_per_person:
            page_per_person = (min_page_per_person + max_page_per_person) // 2
            person_needed = self.get_person_needed(pages, page_per_person)
            if person_needed == max_person:
                max_page_per_person = page_per_person
            if person_needed > max_person:
                min_page_per_person = page_per_person
            if person_needed < max_person:
                max_page_per_person = page_per_person

        if self.get_person_needed(pages, min_page_per_person) <= max_person:
            return min_page_per_person
        if self.get_person_needed(pages, max_page_per_person) <= max_person:
            return max_page_per_person

        return max_page_per_person

    def get_person_needed(self, pages: List[int], time_per_person) -> int:
        person_needed = 1  # at least one person copy all books
        page_sum = 0
        for page in pages:
            page_sum += page
            if page_sum > time_per_person:  # need another person
                page_sum = page
                person_needed += 1

        return person_needed
