# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        l, r = 0, len(arr) - 1
        dummy = ListNode(0)
        curr = dummy

        while l <= r:
            if l == r:
                curr.next = arr[l]
                curr = curr.next
                break

            curr.next = arr[l]
            curr = curr.next

            curr.next = arr[r]
            curr = curr.next

            l += 1
            r -= 1

        curr.next = None  # 🔥 critical to avoid cycles
