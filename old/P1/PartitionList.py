# Linked List, Two Pointers
# Adobe 3 Microsoft 2 Bloomberg 2 Apple 3 Facebook 2 Amazon 5
# https://leetcode.com/problems/partition-list/

# Given the head of a linked list and a value x, partition it such that all nodes less than x come
# before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# reconstruct the list
# small/big head nodes for building small/big lists
# merge them after processing all node
class PartitionList:
    def partition(self, head: Optional[ListNode], pivot: int) -> Optional[ListNode]:
        small_head = ListNode()
        small_head.next = head
        big_head = ListNode()

        small_tail = small_head
        big_tail = big_head
        current = head
        while current:
            if current.val > pivot:
                big_tail.next = current
                big_tail = big_tail.next
            elif current.val < pivot:
                small_tail.next = current
                small_tail = small_tail.next
            elif current.val == pivot:
                # pivot value must be at the bigger side
                big_tail.next = current
                big_tail = big_tail.next

            current = current.next

        # combine
        small_tail.next = big_head.next
        big_tail.next = None

        return small_head.next
