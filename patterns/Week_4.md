# Week 4 — Binary Search

## Pattern entry (end of week, synthesized from the notes below)

### Binary search
- Trigger: sorted / semi-sorted list, we can search though it on log(n) time (meaning we will do more than a few lookups)
- Invariant: base idea is to jump from the low / high to see how the middle point fits and move one of the boundaries to the mid value. On top, this idea can be change to find the lowest / highest 
- Complexity: base implementation is very simple. Adapting it to more complex problems is tricky some times (might need to change the evaluation to a proxy or to follow another scale)
- Anchors:
  - Binary Search:
  - Koko Eating Bananas:
  - Find Minimum in Rotated Sorted Array:
  - Search in Rotated Sorted Array:
- Skeleton (optional): 5-10 lines of code from memory, not pasted
```
def binSearch(array: List[int], target: int) -> int:
  l, r = 0, len(array)

  while l <= r:
    m = ((r - l) // 2) + l
    if array[m] > target:
      r = m - 1
    elif array[m] < target:
      l = m + 1
    else:
      return m
  return -1 or m # depending on the problem
  ```

## Problem notes (fill in right after each solve, ~5 lines each)

### Koko Eating Bananas (medium, solved / ...)
- Trigger: no sorted yet the problem provide some logic we can follow to go through the array in some ordered manner 
- Invariant: a proxy for the possibilities (1, max pile in the source array), duration must be lower the h itself
- Move rule: collect the duration a given speed. If bigger than h, go next; else evaluate if the check if the new value (speed / duration) is lower then the current know value. Go next till the end
- Stuck on: I though on ordering the list, have a vanilla bin search and try different speeds computing the duration in a clever way by finding the index that the speed covers in 1 turn, 2 turns, etc. and summing them. This would make everything log(n) search base on indexes 
- Complexity: most difficult prob in this section for me
---

### Find Minimum in Rotated Sorted Array (medium, solved / ...)
- Trigger: pseudo-sorted list. Just need a clever way to find the shift
- Invariant: an adapted version of bin search can give us the index of the lowest value in the array. Then we can calculate the shift
- Move rule: described above
- Complexity: ez
---

### Search in Rotated Sorted Array (medium, solved / ...)
- Trigger: evolution from the problem above. Here we want to return the value.
- Invariant: Only thing is to adapt to the edge cases for when the array is already rotaed more the the array length, etc.
---

### Skienna
On the videos 7 - 9 some very interesting points were cover like:
- Heap / Priority Queue: sort the values in a fully balanced array having at the root the lowest / highest value. 
  - Can also be represent in a simple array. 
  - Important is the buble up and the push down
  - Very recursive DS

- Merge sort: break the array to its atomic values (single elements) in log an and merge each element back
  - so the breaking costs log(n) 
  - every merge cost N (N is the size of the 2 sub arrays)
  - here as for the dynamic arrays totally we compute o(2n)

- Quick sort: we randomly pick a value and dive the array in 2 before and after that element (to have it performing not always great but very good on average). Then we sort all other elements form the 2 sub-arrays either lower o bigger than P. Over time we sort the list
  - the special property is that P is in the correct place after the filtering is completed.
  - then we have 2 sub arrays (log n)
  - interesting here is that we pay O(n) in the beginning, not at the end as merge sort

Other relevant sort methods: selection sort, insertion sort, etc. (less efficient)