# Python for Coding Interviews

## Lists
- `remove()` to remove elements at specified index
- list comprehensions for syntactic sugar over for loops
- `lst.sort()` for sorting list in-place (O(1) space complexity)
- `sorted(lst)` for returning a sorted copy of lst (O(n) space complexity)

## 2D lists
- `[[0] * 3 for _ in range(2)]` for creating a 2D list (grid) of 2 rows and
  3 columns initialized with the value 0
- Note that `lst = [[0] * 3] * 2` uses reference to the same outer list for both rows
  so `lst[0][0] = 1` will set element at index 0 in both rows to 1

## Hash Maps (dicts)
- `collections.defaultdict` for setting default value for keys that don't exist
  in the dict
- `collections.Counter` for histogram using dict
  - `Counter.update` to count from multiple lists
- dict comprehensions for concisely defining dicts
- `keys()`, `values()` and `items()`

## Hash Sets (sets)
- `add()`, `remove()` and `discard()`
- set comprehensions for concisely defining sets

## Heaps/Priority Queues
- heaps are binary trees where every parent has a value less than, or equal to
  any of its children
- `heapq` heaps
- In python, heaps are minimum priority by default (element with lowest priority
  is at root)
- Key property: Parent at index i is ≤ children at $2 * i+1$ and $2 * i+2$, but
  siblings/cousins are not necessarily ordered (note 8 > 3)
- negate the values to implement a max heap

## Sorting
- Python uses Tim Sort which has O(nlogn) time complexity and O(1) space complexity

## Arithmetic
- To round division towards 0, wrap the operation with `int` e.g., `int(2 / 3)`

## Useful things to know
- Speed: distance / time
- log(m*n) = log(m) + log(n)