class UndergroundSystem:

    def __init__(self):
        self.mydict={}
        self.myavgtime={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.mydict:
            return False
        else:
            self.mydict[id]={'time':t,'Station Name': stationName}
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.mydict:
            temp_sname=self.mydict[id]['Station Name']
            temp_time=self.mydict[id]['time']
            del self.mydict[id]
            if temp_sname + '_' + stationName in self.myavgtime:
                self.myavgtime[temp_sname + '_' + stationName][0]+=1
                self.myavgtime[temp_sname + '_' + stationName][1]+=t-temp_time
            else:
                self.myavgtime[temp_sname + '_' + stationName]=[1,t-temp_time]
                    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation + '_' + endStation in self.myavgtime:
            temp=self.myavgtime[startStation + '_' + endStation]
            return temp[1]/temp[0]
        else:
            return None


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)