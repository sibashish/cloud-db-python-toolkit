#!/usr/bin/env python3
"""
Top K Frequent Elements (LeetCode 347)

Pattern: Hash Map Frequency Count (`collections.Counter`) + Fixed-Size Min-Heap (`heapq`)
Practical Application: Identifying the top K most frequent SQL query fingerprints,
error codes, or client IPs from high-volume database logs in O(n log k) time.
"""

from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Return the k most frequent elements in `nums` using a min-heap of size k.

    Strategy:
        1. Count element frequencies in a single O(n) pass using `Counter` ({num: freq}).
        2. Maintain a min-heap of size k storing `(freq, num)` tuples. Placing `freq`
           first ensures `heapq` compares frequencies rather than element values.
        3. Whenever an item's frequency exceeds the smallest frequency in the heap
           (`min_heap[0][0]`), `heappushpop` evicts the weakest candidate.

    Time Complexity:  O(n log k) — O(n) to count frequencies + O(u log k) for u unique items
    Space Complexity: O(n) — stores frequency map and a heap of size k
    """
    if not nums or k < 1:
        return []

    # Step 1: Count every unique item in one pass -> {item: frequency}
    counts = Counter(nums)

    # Step 2: Keep only the top k most frequent (freq, num) pairs in a min-heap
    min_heap: list[tuple[int, int]] = []
    for num, freq in counts.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        elif freq > min_heap[0][0]:
            heapq.heappushpop(min_heap, (freq, num))

    # Step 3: Extract only the elements from the winning tuples
    return [num for freq, num in min_heap]


if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 4, 5, 6, 7, 9, 8, 5, 3, 1]
    k = 3

    top_elements = top_k_frequent(sample_array, k)
    print(f"Input array: {sample_array}")
    print(f"Top {k} most frequent elements: {top_elements}")

    # Frequencies: 5 (4x), 3 (3x), 4 (3x)
    assert set(top_elements) == {3, 4, 5}, f"Expected {{3, 4, 5}}, got {top_elements}"
    print("Assertion passed!")

