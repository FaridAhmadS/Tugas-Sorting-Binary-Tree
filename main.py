
from typing import List, Optional
from collections import deque
import math


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class AdvancedSorter:
    """
    Advanced Sorting Module
    - Merge Sort Array (virtual sublists + single tmp array)
    - Merge Sort Linked List (fast-slow split)
    - Quick Sort with median-of-three pivot
    """

    def sort_array(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        tmp_array = [0] * len(arr)
        self._rec_merge_sort(arr, 0, len(arr) - 1, tmp_array)
        return arr

    def _rec_merge_sort(self, arr, first, last, tmp_array):
        if first >= last:
            return

        mid = (first + last) // 2

        self._rec_merge_sort(arr, first, mid, tmp_array)
        self._rec_merge_sort(arr, mid + 1, last, tmp_array)

        self._merge_virtual(arr, first, mid, last, tmp_array)

    def _merge_virtual(self, arr, left_start, mid, right_end, tmp_array):
        left = left_start
        right = mid + 1
        index = left_start

        # Stable merge
        while left <= mid and right <= right_end:
            if arr[left] <= arr[right]:
                tmp_array[index] = arr[left]
                left += 1
            else:
                tmp_array[index] = arr[right]
                right += 1
            index += 1

        while left <= mid:
            tmp_array[index] = arr[left]
            left += 1
            index += 1

        while right <= right_end:
            tmp_array[index] = arr[right]
            right += 1
            index += 1

        for i in range(left_start, right_end + 1):
            arr[i] = tmp_array[i]

    # =====================================================
    # LINKED LIST MERGE SORT
    # =====================================================

    def sort_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        right_head = self._split_linked_list(head)
        left_head = head

        left_sorted = self.sort_linked_list(left_head)
        right_sorted = self.sort_linked_list(right_head)

        return self._merge_linked_lists(left_sorted, right_sorted)

    def _split_linked_list(self, head: ListNode) -> Optional[ListNode]:
        midPoint = head
        curNode = head.next

        while curNode and curNode.next:
            midPoint = midPoint.next
            curNode = curNode.next.next

        right_head = midPoint.next
        midPoint.next = None

        return right_head

    def _merge_linked_lists(
        self,
        listA: Optional[ListNode],
        listB: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while listA and listB:
            # Stable merge
            if listA.data <= listB.data:
                tail.next = listA
                listA = listA.next
            else:
                tail.next = listB
                listB = listB.next

            tail = tail.next

        tail.next = listA if listA else listB

        return dummy.next

    # =====================================================
    # QUICK SORT (Median of Three)
    # =====================================================

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        max_depth = 2 * math.floor(math.log2(len(arr)))
        self._quick_sort_recursive(arr, 0, len(arr) - 1, 0, max_depth)
        return arr

    def _quick_sort_recursive(self, arr, first, last, depth, max_depth):
        if first >= last:
            return

        # Fallback ke merge sort untuk menghindari O(n²)
        if depth > max_depth:
            temp = arr[first:last + 1]
            self.sort_array(temp)

            for i, value in enumerate(temp):
                arr[first + i] = value
            return

        pivot_pos = self.partition_quick(arr, first, last)

        self._quick_sort_recursive(
            arr,
            first,
            pivot_pos - 1,
            depth + 1,
            max_depth
        )

        self._quick_sort_recursive(
            arr,
            pivot_pos + 1,
            last,
            depth + 1,
            max_depth
        )

    def partition_quick(self, arr: List[int], first: int, last: int) -> int:
        mid = (first + last) // 2

        # Median-of-three
        if arr[first] > arr[mid]:
            arr[first], arr[mid] = arr[mid], arr[first]

        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]

        if arr[mid] > arr[last]:
            arr[mid], arr[last] = arr[last], arr[mid]

        # Taruh median di depan
        arr[first], arr[mid] = arr[mid], arr[first]

        pivot = arr[first]

        left = first + 1
        right = last

        while True:
            while left <= right and arr[left] <= pivot:
                left += 1

            while left <= right and arr[right] > pivot:
                right -= 1

            if left > right:
                break

            arr[left], arr[right] = arr[right], arr[left]

        arr[first], arr[right] = arr[right], arr[first]

        return right


# =========================================================
# EXPRESSION TREE + IN-PLACE HEAPSORT
# =========================================================

class ExprNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExprHeapSorter:
    def __init__(self, expr_str: str):
        self.expr = expr_str
        self.values = []

    def parse_and_evaluate(self):
        tokens = deque(self.expr.replace('(', ' ( ').replace(')', ' ) ').split())
        root = self._build_tree(tokens)

        if tokens:
            raise ValueError("Token tidak valid")

        return self._evaluate(root)

    def _build_tree(self, tokens):
        if not tokens:
            raise ValueError("Ekspresi tidak lengkap")

        token = tokens.popleft()

        if token == '(':
            left = self._build_tree(tokens)

            if not tokens:
                raise ValueError("Operator hilang")

            operator = tokens.popleft()

            node = ExprNode(operator)
            node.left = left
            node.right = self._build_tree(tokens)

            if not tokens or tokens.popleft() != ')':
                raise ValueError("Kurung tutup hilang")

            return node

        if token.isdigit():
            return ExprNode(int(token))

        raise ValueError(f"Token tidak valid: {token}")

    def _evaluate(self, node):
        if isinstance(node.value, int):
            return node.value

        left_val = self._evaluate(node.left)
        right_val = self._evaluate(node.right)

        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                raise ZeroDivisionError("Pembagian dengan nol")
            return left_val / right_val

        raise ValueError("Operator tidak dikenali")

    # =====================================================
    # HEAP
    # =====================================================

    def build_max_heap(self, arr: List[int]):
        n = len(arr)

        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(arr, i, n)

    def _sift_down(self, arr, root, size):
        while True:
            left = 2 * root + 1
            right = 2 * root + 2
            largest = root

            if left < size and arr[left] > arr[largest]:
                largest = left

            if right < size and arr[right] > arr[largest]:
                largest = right

            if largest == root:
                break

            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    def heap_sort(self, arr: List[int]) -> List[int]:
        self.build_max_heap(arr)

        for end in range(len(arr) - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._sift_down(arr, 0, end)

        return arr

    def validate_complete_binary_tree(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= n and right < n:
                return False

        return True


if __name__ == "__main__":
    sorter = AdvancedSorter()

    arr = [9, 4, 1, 7, 3, 8]
    print("Merge Sort:", sorter.sort_array(arr.copy()))
    print("Quick Sort:", sorter.quick_sort(arr.copy()))

    linked = ListNode(4,
             ListNode(2,
             ListNode(7,
             ListNode(1))))

    sorted_linked = sorter.sort_linked_list(linked)

    print("Linked List Sorted:", end=" ")
    while sorted_linked:
        print(sorted_linked.data, end=" ")
        sorted_linked = sorted_linked.next

    print()

    expr = ExprHeapSorter("((8 * 5) + (9 / (7 - 4)))")

    result = expr.parse_and_evaluate()
    print("Expression Result:", result)

    heap_arr = [40, 12, 9, 25, 1, 33, 18]
    print("Heap Sort:", expr.heap_sort(heap_arr))
