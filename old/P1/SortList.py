# Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
# Amazon 4 Apple 4 TikTok 3 Microsoft 2 Google 2 Facebook 4 ByteDance 4 Adobe 2 Bloomberg 4 Uber 3 Yahoo 2
# https://leetcode.com/problems/sort-list/
# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:
# Input: head = []
# Output: []

# mergesort: partition list + merge. quicksort cannot be used as no index access
# time O(nlogn) logn partitions and each partition costs n
# space O(logn) stack space
class SortList:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.partition(head)
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)

        return self.merge(left_sorted, right_sorted)

    # find mid, detach list, return mid
    def partition(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev_slow = None
        slow = head
        fast = head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        if prev_slow:
            prev_slow.next = None

        return slow

    # merge two sorted linked list
    def merge(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        before_head = ListNode(-(2**31))
        tail = before_head
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return before_head.next
