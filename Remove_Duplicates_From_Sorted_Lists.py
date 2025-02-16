from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Handle edge case where the list is empty
        if not head:
            return None

        # Step 2: Initialize pointer to traverse the list
        current = head

        # Step 3: Traverse the linked list
        while current and current.next:
            # Step 4: If the current value is the same as the next value, remove the duplicate
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate node
            else:
                # Step 5: Move to the next unique node
                current = current.next

                # Step 6: Return the modified linked list
        return head
