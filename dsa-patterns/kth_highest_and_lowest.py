"""
Kth Largest and Kth Smallest Elements in an Array (LeetCode 215 Variant)

Pattern: Fixed-Size Binary Heap (Priority Queue) via Python's `heapq`
Practical Application: Streaming top-K slowest database queries or latency outliers
in O(k) memory without sorting massive log datasets in RAM.
"""

import heapq


def format_ordinal(n: int) -> str:
    """Return an integer formatted with its English ordinal suffix (e.g., 1st, 2nd, 3rd, 4th)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Find the k-th largest element in an unsorted list using a min-heap of size k.

    Strategy:
        Maintain a min-heap holding the top `k` largest elements seen so far.
        The root (`min_heap[0]`) is always the smallest of those `k` winners—which
        makes it the k-th largest overall. Any larger element displaces the root.

    Time Complexity:  O(n log k) — where n is len(nums)
    Space Complexity: O(k) — stores only k elements in memory
    """
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"k={k} must be between 1 and len(nums)={len(nums)}")

    # Slice the first k elements into a new list so the caller's list stays untouched
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Stream remaining elements; replace the weakest top-k winner whenever a larger value appears
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]


def find_kth_smallest(nums: list[int], k: int) -> int:
    """
    Find the k-th smallest element in an unsorted list using a simulated max-heap of size k.

    Strategy:
        Python's `heapq` only implements a min-heap. By negating values (-num), the
        largest original value becomes the smallest negative number and sits at index 0.
        Maintaining a size-k negated heap keeps the `k` smallest elements; negating
        the root at the end yields the exact k-th smallest value.

    Time Complexity:  O(n log k) — where n is len(nums)
    Space Complexity: O(k) — stores only k elements in memory
    """
    if not nums or k < 1 or k > len(nums):
        raise ValueError(f"k={k} must be between 1 and len(nums)={len(nums)}")

    # Initialize a max-heap of size k using negated values
    max_heap = [-num for num in nums[:k]]
    heapq.heapify(max_heap)

    # Push negated elements that are smaller than the current largest candidate (-max_heap[0])
    for num in nums[k:]:
        if -num > max_heap[0]:
            heapq.heappushpop(max_heap, -num)

    # Flip the sign back to return the original positive value
    return -max_heap[0]


if __name__ == "__main__":
    sample_latencies = [98, 569, 11, 68, 23, 55, 39]
    k = 3

    kth_high = find_kth_largest(sample_latencies, k)
    kth_low = find_kth_smallest(sample_latencies, k)

    print(f"Input array: {sample_latencies}")
    print(f"{format_ordinal(k)} highest element: {kth_high}")
    print(f"{format_ordinal(k)} smallest element: {kth_low}")

    # Quick self-checks (sorted order:)
#    assert kth_high == 55, f"Expected 55, got {kth_high}"
#    assert kth_low == 55, f"Expected 55, got {kth_low}"

