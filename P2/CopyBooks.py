# https://www.lintcode.com/problem/437/description
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

# These books list in a row and each person can claim a continous range of books. For example,
# one copier can copy the books from i-th to j-th continously, but he can not copy the
# 1st book, 2nd book and 4th book (without 3rd book).

# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?

# Return the shortest time that the slowest copier spends.

from typing import List


class CopyBooks:
    def copy_books(self, pages: List[int], person: int):
        # one person copies all books
        max_time = sum(pages)
        # each person copies one book
        min_time = min(pages)
        return 0
