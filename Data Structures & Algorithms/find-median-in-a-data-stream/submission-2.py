import heapq
class MedianFinder:

    def __init__(self):
        self.heap_min = []
        self.heap_max = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_min,-num)

        if self.heap_min and self.heap_max and -self.heap_min[0] > self.heap_max[0]:
            val = - heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max,val)
        
        if len(self.heap_min) > len(self.heap_max)+1:
            val = - heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max,val)
        if len(self.heap_min) < len(self.heap_max):
            val =  heapq.heappop(self.heap_max)
            heapq.heappush(self.heap_min,-val)


    def findMedian(self) -> float:
        if len(self.heap_min) > len(self.heap_max):
            return -self.heap_min[0]
        return (-self.heap_min[0] + self.heap_max[0])/2 * 1.0
        