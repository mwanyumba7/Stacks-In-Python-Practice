# Importing stacks from our main stack file
from stack import Stack

# Defining the reverse_string function
def reverse_string(stack, input_str):

# The for loop on line 3 iterates over input_str and pushes each character on to stack  
  for i in range(len(input_str)):
    stack.push(input_str[i])
# Then we initialize rev_str as an empty string. We pop off all the elements from the stack and append them to rev_str one by one on line 13 until the stack becomes empty and terminates the while loop on line 12. 
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()
#We return the rev_str below
  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))