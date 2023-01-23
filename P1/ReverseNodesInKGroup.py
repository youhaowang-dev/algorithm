# Linked List, Recursion
# Amazon 14 Microsoft 10 Apple 4 Bloomberg 4 Adobe 4 Google 2 TikTok 2 Capital One 8 Facebook 5 Yahoo 3 ByteDance 3 Zoom 2
# MakeMyTrip 2 Zenefits 2 eBay 3 Uber 3 Snapchat 2 VMware 2 Qualcomm 2 Walmart Global Tech 2 Oracle 2 PayTM 2 Intuit 2 Tesla 2
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [1,2,3,4,5,6,7], k=2
# left, right: 1 3 => 3 5 => 5 7 => 7 None
class ReverseNodesInKGroup:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        before_head = ListNode()
        before_head.next = head
        prev_tail = before_head

        left = head
        right = head
        while right:
            count = 0
            while right and count < k:
                count += 1
                right = right.next
            # right is now at the head of the next k group
            if count == k:
                reversed_head = self.reverse(right, left, k)
                prev_tail.next = reversed_head
                prev_tail = left
                left = right

        return before_head.next

    def reverse(self, prev, current, k):
        for _ in range(k):
            current_next_copy = current.next
            current.next = prev
            prev = current
            current = current_next_copy

        return prev


class ReverseNodesInKGroup2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_reversed_tail = None
        first_reversed_head = None
        current = head
        reverse_start = head

        while current:
            count = 0
            while count < k and current:
                current = current.next
                count += 1

            if count == k:
                reversed_head = self.reverse(reverse_start, k)
                if not first_reversed_head:
                    first_reversed_head = reversed_head
                if prev_reversed_tail:
                    prev_reversed_tail.next = reversed_head

                prev_reversed_tail = reverse_start
                reverse_start = current

        if prev_reversed_tail:
            prev_reversed_tail.next = reverse_start

        return first_reversed_head if first_reversed_head else None

    def reverse(self, head: Optional[ListNode], k: int):
        prev = None
        current = head
        while k > 0:
            next_current = current.next
            current.next = prev
            prev = current
            current = next_current
            k -= 1

        return prev
