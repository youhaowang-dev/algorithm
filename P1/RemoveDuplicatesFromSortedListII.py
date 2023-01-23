# Linked List
# Microsoft 2 Amazon 2 Adobe 2 Facebook 4 Bloomberg 3 Google 2 ByteDance 2 Arista Networks 2
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]


class RemoveDuplicatesFromSortedListII:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before_head = ListNode(-(2**31))
        before_head.next = head

        slow = before_head
        fast = before_head.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                duplicate_val = fast.val
                while fast and fast.val == duplicate_val:
                    fast = fast.next
                # fast is out of duplicates
                slow.next = fast
            else:
                slow = fast
                fast = fast.next

        return before_head.next


#   public ListNode deleteDuplicates(ListNode head) {
#     ListNode beforeHead = new ListNode(Integer.MIN_VALUE);
#     beforeHead.next = head;

#     ListNode slow = beforeHead;
#     ListNode fast = beforeHead.next;
#     while (fast != null) {
#       # detect duplicate
#       if (fast.next != null && fast.next.val == fast.val) {
#         int duplicatedVal = fast.val;
#         # move fast out of duplicates
#         while (fast != null && fast.val == duplicatedVal) {
#           fast = fast.next;
#         }
#         # delete node(s)
#         slow.next = fast;
#       } else {
#         slow = fast;
#         fast = fast.next;
#       }
#     }

#     return beforeHead.next;
#   }
# }
