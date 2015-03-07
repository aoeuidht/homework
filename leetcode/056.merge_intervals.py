# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        tmp = sorted(intervals, key=lambda i: i.start)
        rst = []
        for i in tmp:
            if not rst:
                rst.append(i)
                continue
            o = rst[-1]
            if o.end >= i.start:
                o.end = o.end if o.end > i.end else i.end
            else:
                rst.append(i)
        return rst
