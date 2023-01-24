# Linked List
# Amazon 7 Media.net 4 Apple 3 Microsoft 2 Facebook 6 Google 4 Bloomberg 2 Adobe 2 Yahoo 2 Walmart Global Tech 2 ByteDance 2 Shopee 2
# https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the
# nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]


# position is 1 based index
class ReverseLinkedListII:
    def reverseBetween(
        self, head: Optional[ListNode], left_pos: int, right_pos: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        before_head = ListNode(-(2**31))
        before_head.next = head

        left_prev, left = self.get_target_nodes(before_head, left_pos)
        _, right = self.get_target_nodes(before_head, right_pos)

        first_list_tail = left_prev
        last_list_head = right.next if right else None
        reversed_head, reversed_tail = right, left
        self.reverse_list(left, right)

        if first_list_tail:
            first_list_tail.next = reversed_head
        if reversed_tail:
            reversed_tail.next = last_list_head

        return before_head.next

    def get_target_nodes(self, before_head: ListNode, target_pos: int):
        prev = before_head
        current = before_head.next
        pos = 1
        while current and pos != target_pos:
            pos += 1
            prev = current
            current = current.next

        return (prev, current)

    def reverse_list(self, left: Optional[ListNode], right: Optional[ListNode]) -> None:
        if not left:
            return
        if right:
            right.next = None
        prev = None
        current = left
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
