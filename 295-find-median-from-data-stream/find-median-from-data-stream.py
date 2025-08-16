import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap)>len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    def findMedian(self) -> float:
        return (self.min_heap[0] if len(self.max_heap)<len(self.min_heap) else (-self.max_heap[0]+self.min_heap[0])/2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()