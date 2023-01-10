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


class PartitionList:

    # reconstruct the list
    # small/big head nodes for building small/big lists
    # merge them after processing all node
    def partition(self, head: Optional[ListNode], pivot: int) -> Optional[ListNode]:
        small_head = ListNode(-1)
        small_head.next = head
        big_head = ListNode(-1)

        # pointers for inserted node
        small = small_head
        big = big_head
        current = head
        while current:
            if current.val > pivot:
                big.next = current
                big = big.next
            elif current.val < pivot:
                small.next = current
                small = small.next
            else:
                # pivot value must be at the bigger side
                big.next = current
                big = big.next

            current = current.next

        # connect 2 lists
        small.next = big_head.next
        big.next = None

        return small_head.next
