#The is_match function below takes in two characters as p1 and p2 and evaluates whether they are a valid pair of brackets. For p1 and p2 to match, p1 has to be an opening bracket while p2 has to be the corresponding closing bracket. If p1 and p2 don’t fall in any of the valid conditions, we return False.

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False