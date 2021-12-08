import random
from graphics import *

class Lightning:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def toString(self):
        print(f"i = {self.i}, j = {self.j}")

    def update(self,depth):

        flag = random. randint(1,5)
        new_i = self.i
        new_j = self.j
        if flag == 1: # right
            new_i = new_i +10
        elif flag == 2: #  left
            new_i = new_i -10
        elif flag == 3:# left diagonal
            new_i = new_i -10
            new_j = new_j +10
        elif flag == 4:# right diagonal
            new_i = new_i +10
            new_j = new_j +10
        elif flag == 5:# down
            new_j = new_j +10
            
        

        if not (new_i <= 800 and new_i>=0 and new_j<=800 and new_j>=0):
        
            return self.update(0)
            
            
        self.i = new_i
        self.j = new_j
        
        return self
    
    def get_sequence(self):
        bolt = []
        idx = 0
        bolt.append((self.i,self.j))
        while self.j < 800:
            

            self =  self.update(0)
            bolt.append((self.i,self.j))
            
            idx = idx +1
        return bolt



        