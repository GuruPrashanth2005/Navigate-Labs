import ast

list1_input = input("Enter first list (e.g., [1, 2, 3]): ")
list2_input = input("Enter second list (e.g., [3, 1, 2]): ")

l1 = ast.literal_eval(list1_input)
l2 = ast.literal_eval(list2_input)

def is_cyclic_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    combined = list1 + list1
    
   
    n = len(list1)
    for i in range(n):
        if combined[i : i + n] == list2:
            return True
            
    return False

print("Is rotation:", is_cyclic_rotation(l1, l2))