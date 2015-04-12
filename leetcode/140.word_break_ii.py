class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if not s:
            return []
        if not dict:
            return []
        self.s = s
        self.sl = len(s)
        for d in dict:
            self.lset.add(len(d))
        self.dset = set(dict)

        return self.w_wrapper(0)

    def w_wrapper(self, start):
        if self.rst_cache.has_key(start):
            return self.rst_cache[start]
        rst = []
        for c_len in self.lset:
            end = start + c_len
            #print start, end
            if end > self.sl:
                break
            cand = self.s[start: end]
            if cand in self.dset:
                # is this the last one
                if end == self.sl:
                    rst.append(cand)
                    continue
                r = self.w_wrapper(end)
                for i in r:
                    rst.append('%s %s' % (cand, i))
        self.rst_cache[start] = rst
        return rst

    def __init__(self):
        self.lset = set()
        self.dset = None
        self.sl = 0
        self.s = None
        self.rst_cache = {}

if __name__ == '__main__':
    so = Solution()
    r = so.wordBreak('leetcode', ['leet', 'code', 'codea'])
    print r
    so = Solution()
    r = so.wordBreak('a', ['a'])
    print r
    so = Solution()
    r = so.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    print r
    so = Solution()
    r = so.wordBreak('aaaaaaa', ["aaaa","aa","a"])
    print r
