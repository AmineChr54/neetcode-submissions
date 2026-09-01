import sortedcontainers
class MedianFinder:

    def __init__(self):
        self.l = sortedcontainers.SortedList()
        self.length = 0
        

    def addNum(self, num: int) -> None:
        self.l.add(num)
        self.length += 1

    def findMedian(self) -> float:
        ind_m = self.length // 2
        return float(self.l[ind_m]) if self.length % 2 == 1 else ((self.l[ind_m] + self.l[ind_m - 1]) / 2)
        