#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.checkInInfo = {}
        self.tripInfo = collections.defaultdict(lambda:[0, 0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInInfo[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.checkInInfo.pop(id)
        self.tripInfo[(start_station, stationName)][0] += (t - start_t)
        self.tripInfo[(start_station, stationName)][1] += 1 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(self.tripInfo[(startStation, endStation)][0], self.tripInfo[(startStation,endStation)][1])
        return self.tripInfo[(startStation, endStation)][0] / self.tripInfo[(startStation,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

