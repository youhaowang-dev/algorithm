# Linked List, Two Pointers, Stack, Recursion
# Amazon 9 Apple 5 Microsoft 4 Adobe 3 Facebook 2 Google 2 Yahoo 2 Spotify 2 Bloomberg 4 Intuit 4 ServiceNow 2 VMware 2
# Oracle 3 Grab 2 Nutanix 2 Paypal 2 Qualcomm 2 IXL
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

# partition list, reverse second half, compare, restore, return result
# 1->2->3->2->1->null
# 1->2->3->null and 1->2->null
# compare 1 and 2
class PalindromeLinkedList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        # partition
        list1_tail = self.get_mid(head)
        # reverse list2
        list2_head = list1_tail.next
        list2_head = self.reverse_list(list2_head)

        list1_head = head
        is_palindrome = True
        while list1_head and list2_head:
            if list1_head.val != list2_head.val:
                is_palindrome = False
                break

            list1_head = list1_head.next
            list2_head = list2_head.next
        # reverse back and reconnect before return
        list1_tail.next = self.reverse_list(list2_head)

        return is_palindrome

    def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next

        return prev
