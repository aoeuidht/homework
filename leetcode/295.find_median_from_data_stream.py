import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small_heap = []
        self.big_heap = []
        self.pivort = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if (not self.small_heap) and (self.pivort == None):
            self.pivort = num
            return
        if self.pivort == None:
            max_of_smalls = - self.small_heap[0]
            min_of_bigs = self.big_heap[0]
            if max_of_smalls <= num <= min_of_bigs:
                self.pivort = num
            elif num < max_of_smalls:
                # swap with max_of_smalls
                self.pivort = - heapq.heapreplace(self.small_heap, - num)
            else:
                self.pivort = heapq.heapreplace(self.big_heap, num)
            return
        # when pivort already exists
        if num <= self.pivort:
            small, big = num, self.pivort
        else:
            small, big = self.pivort, num
        self.pivort = None
        heapq.heappush(self.small_heap, - small)
        heapq.heappush(self.big_heap, big)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.pivort == None:
            return (self.big_heap[0] - self.small_heap[0]) / 2.0
        return self.pivort * 1.0


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(1)
mf.addNum(3)
mf.addNum(4)
print mf.findMedian()
