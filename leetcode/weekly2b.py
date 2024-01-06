import queue
 
# A node of BFS traversal
class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level

class Solution:
    def minOperations(self, x, y):
        # To keep track of visited numbers
        # in BFS.
        visit = set()
    
        # Create a queue and enqueue x into it.
        q = queue.Queue()
        n = node(x, 0)
        q.put(n)
    
        # Do BFS starting from x
        while (not q.empty()):
            
            # Remove an item from queue
            curr = q.get()

            if curr.val in visit:
                continue
    
            # If the removed item is target
            # number y, return its level
            if (curr.val == y):
                return curr.level
    
            # Mark dequeued number as visited
            visit.add(curr.val)
    
            # Insert children of t if not visited
            # already
            if (curr.val % 5==0 and curr.val>y):
                q.put(node(curr.val//5, curr.level+1))
            
            if (curr.val % 11==0 and curr.val>y):
                q.put(node(curr.val//11, curr.level+1))

            if (curr.val<10000):
                q.put(node(curr.val+1, curr.level+1))

            if (curr.val >0):
                q.put(node(curr.val-1, curr.level+1))

    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        res = self.minOperations(x,y)
        print(res)
        return res