from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to simplify edge cases
        dummy = ListNode(-1)
        current = dummy  # Pointer to track position in merged list

        # Step 2: Traverse both lists and merge in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                # Attach the smaller node from list1
                current.next = list1
                list1 = list1.next  # Move ahead in list1
            else:
                # Attach the smaller node from list2
                current.next = list2
                list2 = list2.next  # Move ahead in list2

            # Move current pointer ahead
            current = current.next

        # Step 3: Attach the remaining part of the list that is not yet exhausted
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Step 4: Return the merged list (skip the dummy node)
        return dummy.next
