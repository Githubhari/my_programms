    def solve(self, N, K, GeekNum):
        #your code goes here
        li=GeekNum
        for i in range(len(GeekNum),N):
            #print(li[i-K:])
            li.append(sum(li[i-K:]))
        return li[-1]
      """This is a python code which is coded for POD problem in GFG"""
