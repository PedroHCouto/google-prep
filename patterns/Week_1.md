Arrays & hashing. NeetCode section + Skiena Lectures 1–6 (Ch.1–3: Intro to algorithms → Asymptotic notation → Logarithms → Elementary data structures → Dictionary data structures → Hashing). Write your first patterns/ notes. DDIA ch. 1.

# Pattern:
- When problem clear demands search, goes for hash table if pred / successor isn't that important or can be derived via some trick.
- From the hash tables, start with set to clear out the data input might be a good advantage, specially if the problems do not care about the repeated element
- Search for O(1) alternatives before using DS (e.g.: in one problem the trick was to get a range / a difference before doing something else. This reduces the solution from N * LogN to LogN)
- Lists are for when appending are relevant but first check if I can use some hash table like dictionaries and even leverage the keys of list entries (given there are not that much keys or I can reduce the key amount before adding the keys). Afterwards, I gain search for O(1)
- Keep in mind the sorted DS might be a negative asset (for some operations like search, it usually improves, but the expense is insert, delete, etc.). It's all about trade-offs



# Summary:

## Asymptotic Notation 
we want to find a function that got so asymptotic as possible to the behavior our program, so it's representative at the worst case O, best case Omega, both cases but different constants Theta.

## Elemental Data Structures
Base for all more advanced we have and use. Here we interest most for
- What operations does it support (abstract level)
- How they are implemented / cost O(n)

## Dictionary
Elemental data structure that implement 6 operations:
Search, Insert, Delete, Mix, Max, Logical Predecessor / Successor

## Contiguous Data Structure:
- Allocated all at once
- Less flexible, used at once. Very efficient after allocated

## Discrete Data Structure:
- Elements spread whole RAM
- Does not demand a big chunk of RAM
- Each element holds a pointer to the next one (overhead). This overhead can even be about 50 % of the whole unity if the data part is small

## To the actual data structures
### Arrays
- Fixed size, low overhead, a full block of memory dedicated for it
- Less flexible but very memory efficient
- Demands a full block of memory beforehand


### Dynamic Arrays
- Doubles it size (new alloc) every time the base array gets full.
- At N, as it grows in log N, the whole amount RAM allocated is just 2 * N
- **In python tuples and lists**

## (double) Linked Lists
- A collection of elements pointing to the next
- Also pointing to the previous, in the case of double
- Discrete (flexible) DS element
- **Python does not exposes it natively, available via collections.deque**

## Stack & Queue
- Types of array or linked list
- **Stack LIFO, Queue FIFO**

## Binary Search Trees
- One golden rule: for each label, if lower then the node, it is allocates on the left leave else on the right one
- Only two leafs per node
- **Special for generating all operations with O(h). If perfectly balanced, h = log N**
- Min on the left most leaf, Max on the right most
- In-order travers is given by predecessor / successor N times. So N * log N for full traversing

## Hash tables
- Spread data across keys which are provided via a hash function.
- A hash function transform the input into a key that is O(1) to find under the table logic.
- Each element is assigned to it's key and can be search in O(1) as well
- More the one element assigned to the same key is called collisions.
- Good hash functions are easy to compute and distribute the elements as even as possible 
- Hash func may come from a pattern (open addressing - bad when removing elements), module function (reminder from a big number dived by one of the biggest elements possible that makes sense), existing hash functions (python, cryptography, etc.)
- **Hash tables provide at least Search, Insert and delete with O(1).**
- **In python dicts (for hash tables holding more info) or sets (if the hash table is already the info itself)**

# Important
When I got stuck in the NeetCode was specially when I focused too much on the problem details and the DS and forgot the logic.
The best approach would be:
1. Understand and draw / describe the problem on paper
2. Design a high level algorithm to solve it
3. Search the tools (DS) which works best for this