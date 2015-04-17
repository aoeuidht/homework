class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.f_wrapper(num, 0, len(num)-1)

    def f_wrapper(self, num, lo, hi):
        if num[lo] < num[hi]:
            return num[lo]

        v = num[lo]
        if hi - lo < 100:
            for idx in range(lo+1, hi+1):
                _v = num[idx]
                if _v < v:
                    return _v
                v = _v
            return v

        mid_idx = (lo + hi)  / 2
        mid_v = num[mid_idx]
        if mid_v > v:
            # right
            return self.f_wrapper(num, mid_idx, hi)
        elif mid_v < v:
            return self.f_wrapper(num, lo, mid_idx)
        else:
            return min(self.f_wrapper(num, mid_idx, hi),
                       self.f_wrapper(num, lo, mid_idx))
