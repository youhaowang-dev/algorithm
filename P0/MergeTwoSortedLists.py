# Linked List, Recursion
# Amazon 17 Apple 10 Adobe 6 Google 5 Microsoft 4 Facebook 4 Uber 4 Bloomberg 3 Expedia 3 Yahoo 2 Visa 2 Indeed 3 Oracle 3 Accenture 2 Yandex 2 eBay 2 Shopee 2 VMware 5 ByteDance 5 LinkedIn 3 Walmart Global Tech 3 Intuit 2 GoDaddy 2 Roblox 2 Wix
# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative
class MergeTwoSortedLists:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode(float("-inf"))
        tail = head

        list1_head = list1
        list2_head = list2
        while list1_head and list2_head:
            # dont do if... if... as the pointers can go out of bound after one if
            if list1_head.val < list2_head.val:
                tail.next = list1_head
                list1_head = list1_head.next
            elif list1_head.val > list2_head.val:
                tail.next = list2_head
                list2_head = list2_head.next
            else:
                tail.next = list2_head
                list2_head = list2_head.next

            tail = tail.next

        if list1_head:
            tail.next = list1_head

        if list2_head:
            tail.next = list2_head

        return head.next


class MergeTwoSortedLists2:
    def mergeTwoLists(
        self, list1_head: Optional[ListNode], list2_head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1_head:
            return list2_head
        elif not list2_head:
            return list1_head
        elif list1_head.val < list2_head.val:
            list1_head.next = self.mergeTwoLists(list1_head.next, list2_head)
            return list1_head
        else:
            list2_head.next = self.mergeTwoLists(list1_head, list2_head.next)
            return list2_head
