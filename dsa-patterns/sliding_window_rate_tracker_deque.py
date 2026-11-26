#!/usr/bin/env python3
"""
Number of Recent Calls (LeetCode 933)

Pattern: Sliding Window via `collections.deque`
Practical Application: Counting active database connections or query requests
within a rolling 3,000ms window in O(1) amortized time per call.
"""

from collections import deque


class RecentCounter:
    """Counts incoming requests within the inclusive range [t - 3000, t]."""

    def __init__(self) -> None:
        self.requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """
        Record a request at timestamp `t` (ms) and return total requests
        in the last 3,000ms.

        Time Complexity:  O(1) amortized (each timestamp is added and removed once)
        Space Complexity: O(W) where W is max requests inside a 3,000ms window
        """
        self.requests.append(t)

        # Evict timestamps older than [t - 3000, t] from the left end
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)


if __name__ == "__main__":
    obj = RecentCounter()
    sample_pings = [1, 100, 3001, 3002]

    for idx, timestamp in enumerate(sample_pings, start=1):
        active_count = obj.ping(timestamp)
        print(f"ping({timestamp}) -> param_{idx} = {active_count}")

