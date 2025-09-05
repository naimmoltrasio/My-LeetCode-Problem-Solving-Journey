class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))