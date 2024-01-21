from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_number(l1: ListNode):
    if l1.next is None:
        return l1.val
    return get_number(l1.next) * 10 + l1.val


def set_number(number: int):
    if len(str(number)) == 1:
        return ListNode(val=number)
    return ListNode(val=number % 10, next=set_number(number // 10))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        two_sum = get_number(l1) + get_number(l2)
        return set_number(two_sum)
