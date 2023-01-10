# Linked List, Two Pointers, Stack, Recursion
# Amazon 9 Apple 5 Microsoft 4 Adobe 3 Facebook 2 Google 2 Yahoo 2 Spotify 2 Bloomberg 4 Intuit 4 ServiceNow 2 VMware 2 Oracle 3 Grab 2 Nutanix 2 Paypal 2 Qualcomm 2 IXL
# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# brute force: copy to list then use two pointers

# modify the input to reverse second half, compare, restore
# 1->2->3->2->1->null
# 1->2->3->null and 1->2->null
# compare 1 and 2
class PalindromeLinkedList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        # list1: first half, list2: second half
        list1_tail = self.list1_tail(head)
        list2_head = self.reverse_list(list1_tail.next)

        list1_pointer = head
        list2_pointer = list2_head
        while list1_pointer and list2_pointer:
            if list1_pointer.val != list2_pointer.val:
                # restore
                list1_tail.next = self.reverse_list(list2_head)
                return False
            list1_pointer = list1_pointer.next
            list2_pointer = list2_pointer.next

        # restore
        list1_tail.next = self.reverse_list(list2_head)
        return True

    def list1_tail(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            current_next_copy = current.next
            current.next = prev
            prev = current
            current = current_next_copy

        return prev
