# Hash Table, Linked List, Two Pointers
# Amazon 8 Apple 7 Adobe 4 Bloomberg 3 Cisco 2 Spotify 5 Google 3 Goldman Sachs 3 Oracle 3 Microsoft 2 Yahoo 2
# Visa 6 Nvidia 4 Facebook 3 Intel 3 Salesforce 3 Sprinklr 2 Splunk 2
# https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by
# continuously following the next pointer. Internally, pos is used to denote the index of the node that
# tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


class LinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


class LinkedListCycle2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        visited = set()
        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
