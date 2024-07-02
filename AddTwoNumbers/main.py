class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:
        def addTwoNumbers(self,l1,l2):
            temp = l1
            temp2 = l2
            check = temp
            p = ""
            q = ""
            while temp != None:
                p = p+str(temp.value)
                temp = temp.next
            while temp2 != None:
                q = q+str(temp2.value)
                temp2 = temp2.next
            p = p[::-1]
            q = q[::-1]
                
            sum = int(p)+int(q)
            print(sum)
            sum = str(sum)
            sum = sum[::-1]
            temp = ListNode(0)
            check = temp
            check2 = temp
            count = 0
            for i in range(len(sum)-1):
                temp.next = ListNode(0)
                temp = temp.next
                count+=1
            print(count)
            i = 0
            while check2 != None:
                check2.value = sum[i]
                check2 = check2.next
                i+=1
            return check

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