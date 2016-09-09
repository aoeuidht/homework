class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.num = num
        self.nl = len(num)

        if (self.nl < 1):
            return False

        for i in range(1, self.nl / 2 + 1):
            init_val = int(self.num[:i])
            for j in range(i+1, self.nl):
                left_val = int(self.num[i:j])
                if self.chk(init_val, left_val, j):
                    return True
                if self.num[i] == '0':
                    break
            if self.num[0] == '0':
                break
        return False

    def num_digs(self, num):
        """

        Arguments:
        - `self`:
        - `num`:
        """
        nlen = 0
        while num > 0:
            nlen += 1
            num /= 10
        return nlen if nlen else 1


    def chk(self, init_val, left_val, pos):
        """

        Arguments:
        - `self`:
        - `left_val`:
        - `pos`: notice that pos starts with 0
        """
        # print init_val, left_val, self.num[pos:]
        left_sum = init_val + left_val
        left_len = self.num_digs(left_sum)
        right_len = self.nl - pos
        if left_len > right_len:
            return False
        elif left_len == right_len:
            if left_sum == int(self.num[pos:]):
                return True
            return False
        new_pos = pos + left_len
        print pos, new_pos
        if left_sum == int(self.num[pos:new_pos]):
            return self.chk(left_val, left_sum, new_pos)
        else:
            return False

import sys

if __name__ == '__main__':
    s = Solution()
    print s.isAdditiveNumber(sys.argv[1])
