class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s:
            return True
        if not dict:
            return False
        lset = set()
        for d in dict:
            lset.add(len(d))
        dset = set(dict)
        sl = len(s)
        dp = [0] * sl
        for i in range(-1, sl):
            if (i > -1) and (dp[i] < 1):
                continue
            start = i+1
            for l in lset:
                end = l+i+1
                if end > sl:
                    continue
                _s = s[start:end]
                if _s in dset:
                    dp[end-1] = 1
            if dp[-1] > 0:
                return True
        return dp[-1] > 0

if __name__ == '__main__':
    s = Solution()
    r = s.wordBreak('leetcode', ['leet', 'code', 'codea'])
    print r
    r = s.wordBreak('a', ['a'])
    print r
