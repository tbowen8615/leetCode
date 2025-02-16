from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize two pointers
        prev = None  # Tracks the reversed list
        current = head  # Iterates through the original list

        # Step 2: Traverse the linked list
        while current:
            # Step 3: Store the next node before reversing the pointer
            next_node = current.next

            # Step 4: Reverse the pointer direction
            current.next = prev

            # Step 5: Move prev and current one step forward
            prev = current
            current = next_node

            # Step 6: Return the new head of the reversed list
        return prev
