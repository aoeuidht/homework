class Solution(object):
    def addOperators1(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        self.num = num
        self.nl = len(num)
        self.target = target
        if self.nl == 1:
            return [target] if int(num) == target else []

        self.opmap = ((2, '+', lambda x, y: x + y),
                      (2, '-', lambda x, y: x - y),
                      (10, '*', lambda x, y: x * y),
                      (100, '', lambda x, y: x * 10 + y),
        )
        return [item[0][0] for item in self.parser((0, '0', lambda x, y: y), 0)
                if item[0][1] == target]


    def parser(self, op_tuple, pivort):
        """

        Arguments:
        - `val_tuple`: (val_str, val)
        - `op_tuple`: (priority, op_str, op_lambda)
        - `pivort`: the next position to be handled
        """
        new_char = self.num[pivort]
        val_tuple = (new_char, int(new_char))

        if pivort == self.nl - 1:
            return [(val_tuple, None, pivort + 1)]

        new_cands = []
        cands = []

        for _op_tuple in self.opmap:
            op_pri, op_str, op = _op_tuple
            if op_tuple[0] >= op_pri:
                new_cands.append((val_tuple, _op_tuple, pivort + 1))
            elif _op_tuple[1] or val_tuple[1]:

                _cands = self.parser(_op_tuple, pivort + 1)
                for _cand in _cands:
                    new_val_tuple = ('%s%s%s' % (new_char, op_str, _cand[0][0]),
                                     op(val_tuple[1], _cand[0][1]))
                    if (_cand[2] >= self.nl) or (op_tuple[0] >= _cand[1][0]):
                        new_cands.append((new_val_tuple, _cand[1], _cand[2]))
                    else:
                        cands.append((new_val_tuple, _cand[1], _cand[2]))
        ori_op_tuple = op_tuple
        while cands:
            _cand = cands.pop()
            val_tuple, op_tuple, pivort = _cand
            if pivort >= self.nl:
                new_cands.append(_cand)
                continue

            _cands = self.parser(op_tuple, pivort)
            for _cand in _cands:
                new_val = ('%s%s%s' % (val_tuple[0], op_tuple[1], _cand[0][0]),
                           op_tuple[2](val_tuple[1], _cand[0][1]))
                if (_cand[2] >= self.nl) or (ori_op_tuple[0] >= _cand[1][0]):
                    new_cands.append((new_val, _cand[1], _cand[2]))
                else:
                    cands.append((new_val, _cand[1], _cand[2]))
        return new_cands

if __name__ == '__main__':
    import sys
    s = Solution()
    rsts = s.addOperators(sys.argv[1], int(sys.argv[2]))
    for rst in rsts:
        print rst
    print len(rsts)
