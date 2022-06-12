# Importing stack and main to avoid errors
from stack import Stack
from main import is_match

# Defining is_paren_balanced function in line 6 and On lines 7-9, we declare a stack, s and two variables is_balanced and index, which are set to True and 0, respectively.
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
#Below we declare a while loop ,on line 11, which will execute if the index is less than the length of paren-string and is_balanced is equal to True. If any of the conditions evaluate to False, our program will exit the while loop. In the while loop, we iterate over each character of the paren_string by indexing using the index variable and save the indexed element in paren variable.
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
#We check on line 14 whether paren is any type of the opening brackets and if it is, we push it onto the stack. If it’s not any type of the opening brackets, we check if stack s is empty and set is_balanced to False. This handles our special case.
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
#If the stack is not empty, we pop off the top element and check if the current paren, i.e., a closing bracket matches the type of the top element which is supposed to be an opening bracket. If the types don’t match, then we update is_balanced to False.              
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
# We increment the index for the next iteration. The while loop keeps executing until the index is equal to or greater than the length of paren_string or is_balanced equals False.                  
        index += 1
# After we exit the while loop, on line 21, we check if the stack is empty and is_balanced is True, then we return True. Otherwise, we return False.
    if s.is_empty() and is_balanced:
        return True
    else:
        return False