# Linked List, Recursion
# Apple 2 Google 4 Amazon 3 Adobe 3 Bloomberg 2 Facebook 12 Microsoft 5
# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
class RemoveLinkedListElements:
    def removeElements(
        self, head: Optional[ListNode], target: int
    ) -> Optional[ListNode]:
        if not head:
            return head

        before_head = ListNode(-(2**31))
        before_head.next = head
        current = before_head
        while current.next:
            next_node = current.next
            if next_node.val == target:
                current.next = next_node.next
            else:
                current = current.next

        return before_head.next
