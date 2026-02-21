from node.base import ListNode

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = carry 

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

        return dummy.next



def to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

# --- Testing ---
l1 = to_linked_list([2, 4, 3]) # Represents 342
l2 = to_linked_list([5, 6, 4]) # Represents 465
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print_linked_list(result) # Expected: 7 -> 0 -> 8 (which is 807)
