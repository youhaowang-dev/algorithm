# Hash Table, Linked List, Two Pointers
# Airbnb 3 Bloomberg 2 Apple 2 Microsoft 9 Amazon 8 LinkedIn 4 TikTok 4 Facebook 3 Adobe 3 Nvidia 3 Oracle 2 ByteDance 3 Intuit 3 Qualcomm 2 Uber 2 Google 2 Goldman Sachs 2 Samsung 2 Spotify 2 Nutanix 2
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

# example
#    4->1
#         => 8->4->5
# 5->6->1
# the intersect node is 8

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# two pointers time m+n space 1
class IntersectionofTwoLinkedLists:
    def getIntersectionNode(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1 or not head2:
            return None

        list1_length = self.get_length(head1)
        list2_length = self.get_length(head2)

        list1_pointer = head1
        list2_pointer = head2
        for _ in range(0, abs(list1_length - list2_length)):
            if list1_length > list2_length:
                list1_pointer = list1_pointer.next
            else:
                list2_pointer = list2_pointer.next

        while list1_pointer and list2_pointer:
            if list1_pointer == list2_pointer:
                return list1_pointer

            list1_pointer = list1_pointer.next
            list2_pointer = list2_pointer.next

        return None

    def get_length(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next

        return length


# brute force m*n: For each node in list A, traverse over list B and check if the node also in list B.
class IntersectionofTwoLinkedLists3:
    def getIntersectionNode(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1 or not head2:
            return None

        head1_pointer = head1
        while head1_pointer:
            head2_pointer = head2
            while head2_pointer:
                if head1_pointer == head2_pointer:
                    return head1_pointer
                head2_pointer = head2_pointer.next
            head1_pointer = head1_pointer.next

        return None


# hash set, time m+n, space m
class IntersectionofTwoLinkedLists2:
    def getIntersectionNode(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        visited = set()

        while head1:
            visited.add(head1)
            head1 = head1.next

        while head2:
            if head2 in visited:
                return head2
            head2 = head2.next

        return None
