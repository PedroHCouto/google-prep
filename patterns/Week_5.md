# Week 5 — Linked Lists

## Layout

1. **Pattern entries** — synthesize at week end (one per sub-pattern you actually used)
2. **Per-problem notes** — fill right after each solve
3. **From-scratch implementations** — fast/slow, reversal, merge
4. **Cross-links** — connections to earlier weeks

---

## 1. Pattern entries

> Linked lists tend to split into a few sub-patterns. Keep the ones you used; delete the rest.

### 1a. Dummy (sentinel) head

* **Trigger:** Need to add something before the head (invert a linked list) or head needs to move over the elements
* **Invariant:** Dummy node pointing to the LL head
* Complexity: Simple but strong and usefull
* **Breaks when:** -
* **Anchors:** -
* **Skeleton (from memory, optional):**

```python
dummy = Node(node, next=head)
...
dummy.next = rotated_node
rotated_node.next = head
```

### 1b. Fast / slow pointers

* **Trigger:** Perform opperations somewhere in the LL. The fast point travels up to a point and slow follows performing whatever is needed (invert in k-size group)
* **Invariant:** One pointer travelling faster then the slow
* **Complexity:** Simple
* **Breaks when:** have to account to edge cases like fast gets to the end of the LL before the desired condition
* **Anchors:** great to find circular cases
* **Skeleton (from memory, optional):**

```python
dummy = Node(None, next=head)
slow = fast = head
for i in range(N):
  fast = fast.next

prev = slow
slow = slow.next
while slow != fast:
  prev.next = slow.next # remove the node
  slow.next = dummy.next # now the removed node points to the head
  dummy.next = slow # insert it defenitively behind the head node  
```

### 1c. In-place reversal

* **Trigger:** Takes the node and places it before the current head (a dummy node is also helpful)
* **Invariant:** in each iteration remove the node (prev & next) add it after the sentinel and the current head
* **Complexity:** simple
* **Breaks when:** -
* **Anchors:** revert a list or a sub-set of a list (combine with fast and slow)

### 1d. Merge two sorted lists

* **Trigger:** Collection of lists already sorted (many headers are provided)
* **Invariant:** traverse the nodes and find equal smaller values for efficiency
* **Complexity:** simple
* **Breaks when:** LL of different sizes
* **Anchors:** sorted LL
* **Skeleton (from memory, optional):**

```python
l1 = [...]
l2 = [...]
l3 = [...]
l_nodes = [l1, l2, l3]

###########################


while True:
  control = Defaultdict(list)
  i = 0
  for idx in range(len(l_nodes):
    if l_nodes[idx]:
      control[idx].append[l_nodes[idx]
      if l_nodes[i].val > l_nodes[idx].val:
        i = idx

  if len(control) == 0:
    break
  else:
    # take the nodes and add onto the final merged list...
```

---
