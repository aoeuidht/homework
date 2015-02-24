class Solution:
    # @return a boolean
    def isValid(self, s):
        his = []
        # round brackets, square brackets, braces
        rl, rr, sl, sr, bl, br =  40, 41, 91, 93, 123, 125
        ls = set((rl, sl, bl))
        rd = {rr: rl, sr: sl, br: bl}
        for c in s:
            oc = ord(c)
            if oc in ls:
                his.append(oc)
                continue
            if rd.has_key(oc):
                lc = rd[oc]
                if his and (his.pop() == lc):
                    continue
                return False
        
        return False if his else True
            
        
