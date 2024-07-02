# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        p = ""
        q = ""
        # create p string
        while l1 != None:
            p = p+str(l1.val)
            l1 = l1.next
        # create q string
        while l2 != None:
            q = q+str(l2.val)
            l2 = l2.next
        # reverse p and q
        p = p[::-1]
        q = q[::-1]
        sum = str(int(p)+int(q))[::-1]
        head_node = ListNode(0)
        head_node_copy = head_node
        head_node_copy2 = head_node
        count = 0
        # create a linked list of length equal to the sum
        for i in range(len(sum)-1):
            head_node.next = ListNode(0)
            head_node = head_node.next
            count+=1
        i = 0
        # assign the sum to the linked list
        while head_node_copy2 != None:
            head_node_copy2.val = sum[i]
            head_node_copy2 = head_node_copy2.next
            i+=1
        return head_node_copy

obj = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

obj.addTwoNumbers(l1,l2)
