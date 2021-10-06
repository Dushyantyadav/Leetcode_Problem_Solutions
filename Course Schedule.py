class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mymap={i:[] for i in range(numCourses)}
        for cr,pr in prerequisites:
            mymap[cr].append(pr)
        myset=set()
        
        def mydfs(cr):
            if cr in myset:
                return False
            if mymap[cr]==[]:
                return True
            myset.add(cr)
            for pr in mymap[cr]:
                if not mydfs(pr):return False
            myset.remove(cr)
            mymap[cr]=[]
            return True
        for cr in range(numCourses):
            return mydfs(cr)