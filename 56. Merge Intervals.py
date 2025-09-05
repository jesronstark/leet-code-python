








eclass Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            previous = merged[-1]
            if current[0] <= previous[1]:  # Overlapping intervals
                previous[1] = max(previous[1], current[1])  # Merge
            else:
                merged.append(current)

        return merged
