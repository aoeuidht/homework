# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '%d ~ %d' % (self.start, self.end)

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        hi = len(intervals) -1
        if hi < 0:
            return [newInterval]
        # find the target position
        idx = self.search_interval(intervals, 0, hi, newInterval)
        rst = []
        # the smaller ones
        if idx >= 0:
            rst = intervals[:idx+1]

        #print rst
        # the merge operation
        if rst and rst[-1].end >= newInterval.start:
            rst[-1].end = (rst[-1].end
                           if rst[-1].end > newInterval.end
                           else newInterval.end)
        else:
            rst.append(newInterval)

        #print rst
        # add the following with overlap
        while idx < hi:
            idx += 1
            if intervals[idx].start <= rst[-1].end:
                rst[-1].end = (rst[-1].end if
                               rst[-1].end >= intervals[idx].end
                               else intervals[idx].end)
            else:
                rst.append(intervals[idx])
                break
        #print rst
        if idx < hi:
            rst += intervals[idx+1:]
        return rst

    def search_interval(self, intervals, lo, hi, tgt):
        if lo + 4 > hi:
            for i in range(lo, hi+1):
                if tgt.start <= intervals[i].start:
                    return i - 1
            return hi

        mid = (lo + hi) / 2
        if tgt.start < intervals[mid].start:
            return self.search_interval(intervals, lo, mid, tgt)
        return self.search_interval(intervals, mid, hi, tgt)

if __name__ == '__main__':
    s = Solution()
    print s.insert([Interval(1, 5)], Interval(0,0))
    print s.insert([Interval(1, 5)], Interval(0,6))
    print s.insert([Interval(1, 5)], Interval(1,6))
    print s.insert([Interval(1, 5)], Interval(2,6))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(8, 9))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(1, 9))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(5, 9))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(6, 9))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(6, 19))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(6, 20))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(6, 25))
    print s.insert([Interval(1, 5), Interval(20, 22)], Interval(35, 39))
    print s.insert([Interval(2, 5), Interval(6,7)], Interval(0,1))
