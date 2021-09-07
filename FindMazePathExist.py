class FindMazePathExist:
     
    def __init__(self, V):
         
        self.V = V
         
        # If there are no edges
        self.g = [[0 for j in range(self.V + 1)]
                     for i in range(self.V + 1)]
     
   
        for i in range(self.V + 1):
            self.g[i][i] = 1
 
    def addingEdges(self, v, w):
 
        self.g[v][w] = 1
        self.g[w][v] = 1
 
    def PathsExists(self):
        for k in range(1, self.V + 1):
            for i in range(1, self.V + 1):
                for j in range(1, self.V + 1):
                    self.g[i][j] = (self.g[i][j] |(self.g[i][k] and self.g[k][j]))
    def isReachable(self, s, d):
 
        if (self.g[s][d] == 1):
            return True
        else:
            return False
if __name__=='__main__':
 
    f = FindMazePathExist(7)
    f.addingEdges(4, 4)
    f.addingEdges(1, 2)
    f.addingEdges(3, 2)
    f.addingEdges(4, 3)
    f.addingEdges(1, 4)
    f.addingEdges(1, 4)
    f.PathsExists()
 
    u = 4
    v = 4
     
    if (f.isReachable(u, v)):
        print('1')
    else:
        print('0')
         
