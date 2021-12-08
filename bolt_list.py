from flash import *
from graphics import *

# Bolt list is a list of random sequences
# each sequence starts at (125n, 0), where 1<=n<=7
# and navigates to some point (x, 800)
class BoltList:
    def __init__(self):
        self.list = get_list()
        self.size = 8
    
    
    def get_list(self):
        j = 0
        count =0
        while j < 800:
            
            self.list.append(Lightning(j,0).get_sequence())
            j = j+ 125
            count = count +1
        
    
    def get_size(self):
        return self.size
    
    #returns a 2-tuple (<size>, <index>)
    def min_sequence(self):
        min_size = 1000
        min_idx = 0
        idx = 0
        for i in self.list:
            if len(i) < min_size:
                min_size = len(i)
                min_idx = idx
            idx = idx + 1
        
        return (min_size,min_idx)
    
    

   

        
    
def get_list():
    bolts = []
    j = 0
    
    while j < 800:
        
        bolts.append(Lightning(j,0).get_sequence())
        j = j+ 125
        
    
    return bolts


