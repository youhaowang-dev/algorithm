# Linked List, Recursion
# Amazon 10 Apple 6 Bloomberg 4 Microsoft 3 Adobe 3 Oracle 3 Google 2 Uber 2 Nagarro 2 Facebook 4 Yandex 3 VMware 3 ServiceNow 3 Paypal 2 Intuit 2 Nvidia 2 Yahoo 2 Samsung 2 Dell 2 JPMorgan 2 Canonical 2 IBM 5 Qualcomm 5 Cisco 5 eBay 4 ByteDance 3 Goldman Sachs 2 PayTM 2 Hotstar 2 HBO 2 Snapchat Zenefits Yelp Twitter
# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# two pointers moves at the same speed
# prev will stop at the last node(the reversed list head), current will stop at null
class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        current = head
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next

        return prev
