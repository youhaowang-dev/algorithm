# Linked List
# Amazon 4 Google 3 Yahoo 2 Apple 2 Facebook 2 Adobe 2 Oracle 2 Microsoft 7 Bloomberg 5 eBay 2 VMware 2 TikTok 2
# https://leetcode.com/problems/odd-even-linked-list/

# Given the head of a singly linked list, group all the nodes with odd indices together
# followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# build two lists for odd and even, then connect them
class OddEvenLinkedList:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        index = 1
        odd_tail = head
        even_tail = head.next
        even_head = even_tail
        current = even_tail.next
        while current:
            if index % 2 == 0:
                even_tail.next = current
                even_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
            current = current.next
            index += 1

        even_tail.next = None
        odd_tail.next = even_head

        return head


# build two lists for odd and even, then connect them
class OddEvenLinkedList2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        odd_tail = head
        even_tail = head.next
        even_head = even_tail
        # move forward by 2 steps
        while even_tail and even_tail.next:
            next_odd = odd_tail.next.next
            next_even = even_tail.next.next

            odd_tail.next = next_odd
            even_tail.next = next_even

            odd_tail = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head

        return head
