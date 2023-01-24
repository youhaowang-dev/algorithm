# Hash Table, Linked List
# Amazon 23 Facebook 8 Bloomberg 6 Microsoft 3 Apple 3 Adobe 4 Google 3 ByteDance 2 Qualtrics 8 eBay 7
# VMware 4 Nvidia 3 Yahoo 3 Oracle 3 Walmart Global Tech 3 ServiceNow 2 Intel 2 Uber Wix
# https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional random pointer, which
# could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where
# each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
# the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list,
# where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


class CopyListWithRandomPointer:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        node_to_copy = self.copy_nodes(head)
        self.copy_pointers(head, node_to_copy)

        return node_to_copy.get(head)

    def copy_nodes(self, node):
        node_to_copy = dict()
        while node:
            node_to_copy[node] = ListNode(node.val)
            node = node.next

        return node_to_copy

    def copy_pointers(self, node, node_to_copy):
        while node:
            copy = node_to_copy.get(node)
            copy.next = node_to_copy.get(node.next)
            copy.random = node_to_copy.get(node.random)
            node = node.next


# O(1) space but will modify input
# Inserting the cloned node just next to the original node.
# If A->B->C is the original linked list,
# Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
class CopyListWithRandomPointer2:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        self.append_copy_to_next(head)
        copy_head = head.next
        self.copy_randoms(head)
        self.separate_nodes(head)

        return copy_head

    def append_copy_to_next(self, node):
        while node:
            node_next = node.next
            copy = ListNode(node.val)
            node.next = copy
            copy.next = node_next

            node = node.next.next

    def copy_randoms(self, node):
        while node:
            copy = node.next
            random_copy = node.random.next if node.random else None
            copy.random = random_copy

            node = node.next.next

    def separate_nodes(self, node):
        while node:
            next_node = node.next.next
            copy = node.next
            next_copy = next_node.next if next_node else None

            copy.next = next_copy
            node.next = next_node

            node = next_node
