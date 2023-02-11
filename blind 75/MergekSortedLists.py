# Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
# Amazon 41 Microsoft 5 Uber 5 Facebook 5 Apple 4 Google 4 Adobe 3 Walmart Global Tech 3 Indeed 2 Bloomberg 2 Zillow 2
# Media.net 2 ByteDance 10 VMware 5 LinkedIn 4 TikTok 4 Shopee 3 Sprinklr 3 Snapchat 2 Oracle 2 Goldman Sachs 2 Yandex 2
# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []


# divide and conquer, time nlogk for logk merges, space
class MergeKSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])

        return self.merge_two_lists(list1, list2)

    def merge_two_lists(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1

        before_head = ListNode()
        tail = before_head
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return before_head.next

# min heap O(nlogk), can also use (val, node) instead of __lt
class MergeKSortedLists2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        before_head = ListNode()
        tail = before_head

        min_heap = list()
        for node in lists:
            if node:
                heappush(min_heap, node)

        while min_heap:
            min_node = heappop(min_heap)
            tail.next = min_node
            tail = tail.next
            if min_node.next:
                heappush(min_heap, min_node.next)

        return before_head.next
