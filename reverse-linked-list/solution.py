import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def instinct(self, head: ListNode) -> ListNode:
        """This is O(n) time and space complexity since I used an additional stack"""
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        head, tail = stack.pop()

        while stack:
            tail.next = stack.pop()
            tail = tail.next

        return head

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


class TestInstinctSolution(unittest.TestCase):
    def create_linked_list(items: lst[int]) -> ListNode:
        head, tail = ListNode(items.remove(0))
        for i, val in enumerate(items):

    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
