# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
    length, offset = 1, 0
    
    curr = head
    while curr.next != None:
        length += 1
        curr = curr.next
    
    if n == length:
        head = head.next
    else:
        offset = length - n - 1
        
        i = 0
        curr = head
        while i < offset:
            curr = curr.next
            i += 1

        curr.next = curr.next.next

    return head