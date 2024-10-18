

class Node:

    # construct this Node with the given id
    def __init__(self, id):
        # used for Dijkstra's implementation
        self.cost = 0.0
        self.predecessor = None
        self.id = id
        self.outgoing = []
        
    def __repr__(self):
        return str(self)
        
    # returns True if this node is a thru node
    def isThruNode(self):
        return True
    
  
    def __str__(self):
        return str(self.id)
    
    # adds ij to list of outgoing links
    def addOutgoingLink(self, ij):
        if ij.start == self:
            self.outgoing.append(ij)
