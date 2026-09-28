# Assignment 3: Understanding Algorithm Efficiency and Scalability

## Overview

This project analyzes the efficiency and scalability of two important algorithmic techniques:

1. Randomized Quicksort
2. Hash Table with Chaining

The project also compares Randomized Quicksort with Deterministic Quicksort using the first element as the pivot. The comparison uses different input sizes and distributions to examine how pivot selection affects performance.

## Project Files

- `quicksort.py` - Implements Randomized Quicksort and tests several edge cases.
- `hash_table.py` - Implements a hash table using separate chaining and a deterministic polynomial hash function.
- `performance_test.py` - Empirically compares Randomized and Deterministic Quicksort.
- `README.md` - Provides project information, execution instructions, and a summary of findings.
- `Assignment3_Final_Rachana_Peddi.docx` - Contains the theoretical analysis, empirical results, and discussion.

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run the Project

Open a terminal in the project directory.

### Run Randomized Quicksort

```bash
python quicksort.py
```

The program tests:

- Random input
- Repeated elements
- Already sorted input
- Reverse-sorted input
- Empty input
- Single-element input

### Run Hash Table with Chaining

```bash
python hash_table.py
```

The program demonstrates:

- Insert operations
- Search operations
- Updating an existing key
- Delete operations
- Missing-key handling
- Collision handling through separate chaining
- Polynomial hashing
- Load-factor calculation
- Dynamic resizing and rehashing

### Run the Quicksort Performance Comparison

```bash
python performance_test.py
```

The experiment compares Randomized Quicksort with Deterministic Quicksort using the first element as the pivot.

Four input distributions are tested:

- Random
- Already sorted
- Reverse sorted
- Repeated elements

The tested input sizes are:

- 100
- 500
- 1,000
- 2,000

Each timing measurement is averaged over five trials.

## Summary of Findings

The experiments showed that input distribution has a significant effect on Deterministic Quicksort when the first element is always selected as the pivot.

For random input, both algorithms produced relatively similar execution times. At an input size of 2,000, Randomized Quicksort required approximately 0.003229 seconds, while Deterministic Quicksort required approximately 0.003273 seconds.

A much larger difference appeared with already sorted input. At an input size of 2,000, Randomized Quicksort required approximately 0.002821 seconds, compared with approximately 0.158595 seconds for Deterministic Quicksort.

The difference was also substantial for reverse-sorted input. At an input size of 2,000, Randomized Quicksort required approximately 0.003803 seconds, while Deterministic Quicksort required approximately 0.223421 seconds.

For repeated elements, both implementations performed efficiently in this experiment. At an input size of 2,000, Randomized Quicksort required approximately 0.000574 seconds, while Deterministic Quicksort required approximately 0.000430 seconds.

These results demonstrate that first-element pivot selection can perform poorly on already sorted and reverse-sorted inputs. Random pivot selection reduces the dependence of Quicksort's performance on the original ordering of the input.

## Hash Table Summary

The hash table uses separate chaining to resolve collisions. Each table position contains a bucket that can store multiple key-value pairs.

A deterministic polynomial hash function with a base value of 31 is used to calculate bucket locations for string keys. The implementation supports insert, search, update, and delete operations.

The table also monitors its load factor. When the load factor becomes greater than 0.75, the capacity is doubled and the existing entries are rehashed into the new table. This helps prevent chains from becoming unnecessarily long as additional elements are inserted.

The test execution demonstrated collision handling when multiple keys were placed in the same bucket while remaining independently searchable.

## Conclusion

The project demonstrates how algorithm design and input characteristics affect efficiency and scalability. Randomized Quicksort provides an expected O(n log n) running time and avoids consistently poor behavior caused by fixed pivot selection on ordered inputs.

The hash-table implementation demonstrates how separate chaining resolves collisions and how controlling the load factor through dynamic resizing helps maintain efficient operations.