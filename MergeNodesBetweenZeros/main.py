class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode):
        temp = head
        sums = 0
        res_arr = []
        while temp is not None:
            if temp.val == 0:
                res_arr.append(sums)
                sums = 0
                temp = temp.next
                continue
            sums+= temp.val
            temp = temp.next
        return self.convertToLinkedList(res_arr)

    def convertToLinkedList(self, arr):
        head = ListNode(arr[1])
        temp = head
        for i in range(2, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return head

    def display(self, head):
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next    

def main():
    head = ListNode(0)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(0)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next.next = ListNode(0)
    sol = Solution()
    res = sol.mergeNodes(head)
    sol.display(res)

main()
