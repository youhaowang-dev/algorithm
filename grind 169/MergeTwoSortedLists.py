# Linked List, Recursion
# Amazon 17 Apple 10 Adobe 6 Google 5 Microsoft 4 Facebook 4 Uber 4 Bloomberg 3 Expedia 3 Yahoo 2 Visa 2 Indeed 3 Oracle 3 Accenture 2 Yandex 2 eBay 2 Shopee 2 VMware 5 ByteDance 5 LinkedIn 3 Walmart Global Tech 3 Intuit 2 GoDaddy 2 Roblox 2 Wix
# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists head1 and head2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

from typing import Optional


class MergeTwoSortedLists:  # iterative
    def mergeTwoLists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1

        before_head = ListNode(0)
        tail = before_head

        while head1 and head2:
            # elif is needed pointer can be outbound after head1.next or head2.next, if...if...if won't work
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            elif head1.val > head2.val:
                tail.next = head2
                head2 = head2.next
            elif head1.val == head2.val:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        if head1:
            tail.next = head1

        if head2:
            tail.next = head2

        return before_head.next


class MergeTwoSortedLists2:  # recurisive
    def mergeTwoLists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1:
            return head2
        elif not head2:
            return head1
        elif head1.val < head2.val:
            head1.next = self.mergeTwoLists(head1.next, head2)
            return head1
        elif head1.val >= head2.val:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2
