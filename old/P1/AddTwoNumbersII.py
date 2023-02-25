# Linked List, Math, Stack
# Bloomberg 7 Amazon 3 Microsoft 4 Oracle 3 Capital One 8 Facebook 5 Apple 5 Adobe 3 Goldman Sachs 2 Yahoo 2 Accolite 2 Samsung 2
# https://leetcode.com/problems/add-two-numbers-ii/description/

# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]

# reverse, merge, reverse back
class AddTwoNumbersII:
    def addTwoNumbers(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1

        reversed_head1 = self.reverse(head1)
        reversed_head2 = self.reverse(head2)
        merged_reversed_head = self.merge(reversed_head1, reversed_head2)

        return self.reverse(merged_reversed_head)

    def reverse(self, head: Optional[ListNode]):
        prev = None
        current = head
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next

        return prev

    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        before_head = ListNode()
        carry = 0
        tail = before_head
        while head1 and head2:
            sum = head1.val + head2.val + carry
            carry = sum // 10
            current_digit = sum % 10
            tail.next = ListNode(current_digit)

            tail = tail.next
            head1 = head1.next
            head2 = head2.next

        while head1:
            sum = head1.val + carry
            carry = sum // 10
            current_digit = sum % 10
            tail.next = ListNode(current_digit)

            tail = tail.next
            head1 = head1.next
        while head2:
            sum = head2.val + carry
            carry = sum // 10
            current_digit = sum % 10
            tail.next = ListNode(current_digit)

            tail = tail.next
            head2 = head2.next

        if carry:
            tail.next = ListNode(carry)
            tail = tail.next

        merged_head = before_head.next
        before_head.next = None

        return merged_head
