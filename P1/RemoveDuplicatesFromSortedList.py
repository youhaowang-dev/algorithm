# Linked List, Two Pointers
# Amazon 4 Google 3 Adobe 2 Apple 2 Microsoft 2 Bloomberg 3 Facebook 3 Goldman Sachs 8 Qualcomm 3 Arista Networks 2 ByteDance 2 Paypal 2
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# two pointers slow and fast
# delete while fast moves forward
class RemoveDuplicatesFromSortedList:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        before_head = ListNode(-(2**32))
        before_head.next = head

        slow = before_head
        fast = before_head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next

        return before_head.next
