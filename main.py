# Stack Data Structure
# Below i will be implementing the stack data structure using lists. I will be stacking books

class Stack:
  # I’m defining a class variable that I’m calling items, and I’m assigning it to an empty list
  
  def __init__ (self):
    self.items = []
    
 # self.items is created when we create a stack object so now let’s create the push method:
    
  def push(self,item):