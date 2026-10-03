# Week 2 — Two pointers & sliding window


## Two pointers:
When: 
- Need to move and adjust a window and i can do it growing from somewhere or shrinking from both ends (l, r)
- When there is a clear / well defined window to search
- When I can clearly adjust the window against a given logic to find a stop condition for each pointer

Core / complexity: avoids O(n2) bring it usually to O(n) at no cost of extra space complexity

Gotcha: 
- It was hard to me to understand when to move each pointer. This is what makes the solution simple and elegant
- I didn't consider that for some problems I can and should prepare the input element (sorting, cleaning, etc.) so two pointers become applicable


## Sliding window:
When:
- I have either a fixed type of window or somehow can build a dynamic one to avoid repetitions (lowering big O)
- I have to compare, analyse, find out something within a window (usually fixed is compare, dynamic is to find something like max size of a possible substring given a condition)

Core / complexity: the trick is again to lower the cost of O(n2) to something close to O(n), sometimes O(n * m) or O(n * log n), e.g.: if we build a tree before searching for a condition within the window of size k

Gotcha:
- Fix size are easy to understand but hard to avoid going into many loops while parsing them for the given condition. It's clever too think about any catch to reduce the time complexity further
- Dynamic is really hard to understand which condition to use to update the left side of the window. Here we wanna jump as clever as possible to reduce the subset we need to analyse but to find out how and why was quite hard for me. Focus on this before anything else on those problems
