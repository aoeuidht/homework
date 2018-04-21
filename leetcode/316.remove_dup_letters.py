#! /usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

class Solution(object):
    def __init__(self):
        pass

    def removeDuplicateLetters(self, s):
        """

        Arguments:
        - `self`:

        """
        appr_dict = {}
        rst_array = []
        rst_dict = {}
        idxa = ord('a')

        offset = -1
        for c in s:
            offset += 1
            idx = ord(c) - idxa
            if idx not in appr_dict:
                appr_dict[idx] = []
                appr_dict[idx].append(offset)
            elif offset <> (appr_dict[idx][-1] + 1):
                appr_dict[idx].append(offset)

        last_appr_list = [(j[-1], i) for i, j in appr_dict.iteritems()]
        last_appr_list.sort()

        max_offset = -1
        for k in last_appr_list:
            p_offset, p_idx = k
            if p_idx in rst_dict:
                continue
            print chr(p_idx+idxa), p_offset, self.gen_rst(rst_array)
            for idx in range(p_idx+1):
                if idx not in appr_dict:
                    continue
                if idx in rst_dict:
                    continue
                # 找到第一个比 max-offset 大的
                v = self.get_min_bigger_than(appr_dict[idx], 0, len(appr_dict[idx])-1, max_offset)
                if (v >= 0) and (v <= p_offset):
                    max_offset = v
                    rst_dict[idx] = 1
                    rst_array.append([v, idx])

        return self.gen_rst(rst_array)


    def get_min_bigger_than(self, array, start, end, piv):
        """

        Arguments:
        - `array`:
        - `start`:
        - `end`:
        - `small`:
        - `big`:
        """

        """
        for idx in range(start, end+1):
            if array[idx] > piv:
                return array[idx]
        return -1
        """

        if array[end] <= piv:
            return -1
        elif array[start] > piv:
            return array[start]
        if (end - start) > 10:
            idx = (end + start) / 2
            if array[idx] < piv:
                return self.get_min_bigger_than(array, idx+1, end, piv)
            return  self.get_min_bigger_than(array, start, idx, piv)
        for idx in range(start, end+1):
            if array[idx] > piv:
                return array[idx]


    def gen_rst(self, rst_array):
        idxa = ord('a')
        rst_array = [i for i in rst_array if (i[0] > -1)]
        rst_array.sort()
        rst = ''.join([chr(i[1] + idxa) for i in rst_array])
        return rst




if __name__ == '__main__':
    s = Solution()
    t = 'cbacdcbc'
    print s.removeDuplicateLetters(t), t
    t = 'bcabc'
    print s.removeDuplicateLetters(t), t
    t = 'cbaddabaa'
    print s.removeDuplicateLetters(t), t
    t = "abacb"
    print s.removeDuplicateLetters(t), t
    t = 'c'
    print s.removeDuplicateLetters(t), t
    t = "peymrzknlxtrutjiybqemquchgvtmmtpjvunvekszrkatctcirxwuqknrycpdtcuadblzkkleduezgspoxhhssoipbmdgrqggpfdsanolzczpaggwxrlaleaqtnzxclmxwjucnujsptnbmmjzzjhypnlsoxjveywsufegzlfnyvkcnfevkshbckfropoydkdlblppllgefagjgpajsplvxknvtlgtjyhmnwxcpjjzcizihycvsnhnnmqohivekitxzuo"
    print s.removeDuplicateLetters(t), t, 'abcefghkrdjlmnwpiysqovtxzu'
    t = "yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"
    print s.removeDuplicateLetters(t), t
    t = "yzlydl"
    print s.removeDuplicateLetters(t), t
