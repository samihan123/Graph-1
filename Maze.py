'''
time complexity: O(E+V)
space complexity: O(E+V)
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start==destination: return True
        q = deque([])
        q.append(start[0])
        q.append(start[1])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while(len(q)!=0):
            currR = q.popleft()
            currC = q.popleft()
            for d1,d2 in dirs:
                i = currR 
                j = currC 
                
                while(i>=0 and i<len(maze) and j>=0 and j<len(maze[0]) and maze[i][j]!=1):
                    i+=d1
                    j+=d2
                i-=d1
                j-=d2
                if(i == destination[0] and j == destination[1]): return True
                if(maze[i][j]!=2):
                    q.append(i)
                    q.append(j)
                    maze[i][j]=2
        return False