# Stack Data Structure
# Below i will be implementing the stack data structure using lists. "I will be stacking books"

class Stack:
# I’m defining a class variable that I’m calling items, and I’m assigning it to an empty list
  
  def __init__ (self):
    self.items = []
    
# self.items is created when we create a stack object so now let’s create the push method:

# push is going to be a member of this class, and it’s going to take an item as an argument. In our example, that item is the book. We are putting or pushing the name of the book onto the top of the stack.
    
  def push(self,item):
    self.items.append(item)
    
# The other method we are going to add is the pop method. This method wil return the last element inserted in the list.
    
  def pop(self):
    return self.items.pop()

# We can then add a method is_empty that can tell us if the stack is empty

  def is_empty(self):
    return self.items == []

# We can also add the peek method, whwere we will first check whether the stack is empty and if it isnt we will then return the top most book in the Stack

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    
# We then make a method called get_stack(). This will return the items list, which forms the core of the stack
  
  def get_stack(self):
    return self.items

# I then define a stack object, myStack, and push Cortana and Siri onto the stack

myStack = Stack()
myStack.push("Cortana")
myStack.push("Siri")

# Now lets print my stack to see if my books were added

print("My first books in the stack are :\n")

print(myStack.get_stack())

print("\n 'Cortana' is at the bottom of the stack and 'Siri' is at the top")

print("\n-----------------------------------------------\n")

# Now i will push my new book "Mara" into my Stack

myStack.push("Mara")

print(myStack.get_stack())

print("\n After printing the stack again we see that now 'Mara', my new book, is at the top of the stack")

# Lets now use the is_empty method to see if our stack is empty
print("\n ---------------------------------------")
print("\nChecking if my stack is empty............")
print(f" Is my stack empty : {myStack.is_empty()}")

# Lets now practice the peek method
print("\n -------------------------------------")
print(f"\n The book on top of the stack is : {myStack.peek()}")