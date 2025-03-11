class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            # Check if the current interval overlaps with the last merged interval
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)

        return merged_intervals