# Linked List, Math, Recursion
# Amazon 19 Apple 14 Adobe 12 Microsoft 8 Bloomberg 6 Google 5 IBM 5 Facebook 4 Cisco 3 Expedia 3 Uber 2 Yahoo 2
# PayTM 2 Oracle 5 SAP 2 JPMorgan 2 Capital One 4 eBay 3 Paypal 3 Yandex 3 Huawei 3 Cognizant 3 Twitter 2 Samsung 2
# Goldman Sachs 2 Morgan Stanley 2 Visa 2 ServiceNow 2 tcs 2 Tesla 2 Airbnb Wix
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def addTwoNumbers(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1

        before_head = ListNode(0)
        current = before_head
        carry = 0
        while head1 and head2:
            print(head1, head2)
            sum = carry + head1.val + head2.val
            current.next = ListNode(sum % 10)
            carry = sum // 10
            head1 = head1.next
            head2 = head2.next
            current = current.next

        while head1:
            sum = carry + head1.val
            current.next = ListNode(sum % 10)
            carry = sum // 10
            head1 = head1.next
            current = current.next

        while head2:
            sum = carry + head2.val
            current.next = ListNode(sum % 10)
            carry = sum // 10
            head2 = head2.next
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return before_head.next
