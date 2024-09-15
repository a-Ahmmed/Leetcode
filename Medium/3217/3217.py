# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    prev, curr = head, head

    while prev.next != None:
        if curr == head:
            if head.val in nums:
                head = head.next
                curr = head
                prev = head
            else:
                    curr = curr.next
        else:
            if curr.val in nums:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head

def attempt2(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    prev, curr = None, None

    for i in nums:
        prev, curr = head, head

        while prev.next != None:
            if curr == head:
                if head.val == i:
                    head = head.next
                    curr = head
                    prev = head
                else:
                    curr = curr.next
            else:
                if curr.val == i:
                    prev.next = curr.next
                    curr = prev.next
                else:
                    prev = curr
                    curr = curr.next

def attempt3(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    curr = None
    nums = set(nums)

    while head.val in nums:
        head = head.next 
        
    curr = head
    while curr.next != None:
        if curr.next.val in nums:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head