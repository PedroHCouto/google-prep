# Week 3 — <topic>

## Pattern entry (end of week, synthesized from the notes above)

### Stacks
- Trigger: when we want to progress over a sequence and there is a way to relate the whole analysis to the element at the top of the sequence at a given moment (specially if it's ordered or monotonic de-crescent)
- Invariant: traverse with a for check the stack top (peek) with a while popping the necessary elements
- Complexity: It allows me to reduce some O(n2) over a O(n) problem (even if I need to pass a couple times over the original list, it's still O(n))
- Breaks when: there is no way to handle it in a list looking at the last element
- Anchors:
  - Evaluate Reverse Polish Notation: understanding the rules and translating them to a implementation with stack
  - Daily Temperature: I didn't got when and where to use stack / queue | with some tricks we can create a monotonic decreasing stack and then calculate the band by comparing pop against peek. Here it was where I started to understand when to use stacks
  - Car Fleet: sort, then calculate how many moves a car need till the end, and stack pop/peek to adjust to the no pass allowed rule
- Skeleton (optional): 5-10 lines of code from memory, not pasted
  for i in range(X):
    while True:
      p = stack.pop
      if p > stack[-1]:
        do something  



## Problem notes (fill in right after each solve, ~5 lines each)

### Valid Parenthesis (easy, solved / took longer than I expected)
- Trigger: "Open brackets are closed in the correct order." -> FILO order matters, then use stack
- Invariant: I needed to use dynamic sliding window though
- Move rule: Opening character "{, [, (", then I can register the closing equivalent in a Stack and r+=1. If a closing char comes, compare the last out later (move l & r if last out match)
- Stuck on: took me some minutes to put together sliding window + stack (FILO)
- Complexity: i did in O(n) for time & space
---

### Evaluate Reverse Polish Notation (medium, solved / I made it hard than needed)
- Trigger: understand the polish notation before coding (i did not)
- Invariant: simple stacks based on the simple rule on how to calculate the results and update the stack
- Move rule: pos the last two nums from the stack, do the math and append the new result
- Stuck on: how it functions (the move rule above)
- Complexity: O(n), O(n)
- Obs: recursion would also work here
---

### Daily Temperature (medium, solved / took longer than I expected)
- Trigger: I didn't got when and where to use stack / queue 
- Invariant: stack used in a clever way
- Move rule: with some tricks we can create a monotonic decreasing stack and then calculate the band by comparing pop against peek
- Stuck on: noticing that this approach was possible
- Complexity: O(n) for both
---

### Car Fleet (medium, solved / took longer than I expected)
- Trigger: pattern 1: mix of position and speed (i need the product) | pattern 2: a car cannot pass the other (a stack with pop against peek comparison)
- Invariant: stack with pop and peek technic. As position is important, we need to sort
- Move rule: sort, then calculate how many moves a car need till the end, and stack pop/peek to adjust to the no pass allowed rule
- Stuck on: a bit stuck on applying the stack pop/peek but went fine
- Complexity: O (n log n), O(n)


### Large Rectangle in Histogram (hard, solved / I could only do it brute force)
- Trigger: the algo is complex than I expected and drawing would be fundamental for solving it
- Invariant: with some preparation one can still use stack here (IMPORTANT)
- Move rule: move forward, pop when there is no way to progress and evaluate area (dont pop what is still valid). At the end ona pass to compute final areas
- Stuck on: visualizing this option to solve it
- Complexity: O(n) for both





