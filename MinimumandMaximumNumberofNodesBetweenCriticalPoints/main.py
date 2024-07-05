# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        node = head
        prev = None
        first, last, mini, prev_crit = None, None, None, None
        if head is None:
            return [-1, -1]
        prev = node.val
        node = node.next
        if node.next is None:
            return [-1, -1]

        i = 1
        while True:
            if node is None:
                break

            if Solution.is_crit(node, prev):
                if last is None:
                    first = i
                    last = i
                elif mini is None:
                    mini = i - last
                elif i - last < mini:
                    mini = i - last
                last = i
            prev = node.val
            node = node.next
            i += 1
            pass

        if last is None or last == first:
            return [-1,-1]
        maxi = last - first
        return [mini, maxi]

        pass
    
    def is_crit(node, prev):
        if node.next is None:
            return False
        if node.val > prev and node.val > node.next.val:
            return True
        if node.val < prev and node.val < node.next.val:
            return True
        return False

