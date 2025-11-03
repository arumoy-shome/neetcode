# Time and Space complexity

All complexities are written for Python.

- Any reading/writing operation: O(1) (index/location is known)
- Traverse through a list with *n* elements: O(n)
- Adding/deleting from end (tail) of list: O(1)
- Adding/deleting at i^th^ position: O(1)
- Insertion Sort: worst case O(n^2) best case O(n)
- Merge Sort: O(nlogn)
- Binary search array (BSA): O(logn)
  - Insertion/deletion is O(n) (because we have to shift the other elements)
- Binary search tree (BST): O(logn)
  - Assumption is that the tree is balanced (difference in height of left and
    right subtrees is <= 1); otherwise it's a linked list, so time complexity
    becomes O(n)
  - Advantage of BSTs over BSAs is that insertion/deletion is O(logn) as well
- Hash maps (`dict`): insertion, deletion and searching are all O(1)
  - Reading item in keys of dict (e.g., `k in my_dict`): O(1)
  - Reading item in values of dict (e.g., `v in my_dict.values()`): O(n)
- Space complexity of adjacency matrix: O(V^2) where V is the number of vertices (nodes)

## Worst to best complexity
O(n!) > O(2^n) > O(n^3) > O(n^2)/O(n*m) > O(nlogn) > O(n) > O(logn) > O(1)