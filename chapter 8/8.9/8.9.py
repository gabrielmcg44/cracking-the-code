# ()
# ()() (())
# ()()() (())() ()(()) ((())) (()())

    
def print_parens(available_up, available_down=None, height=0, current_str=""):
    if available_down is None:
        available_down = available_up
    
    if available_down == 0:
        print(current_str)
        
    if available_up > 0:
        print_parens(available_up - 1, available_down, height + 1, current_str + "(")
    
    if height > 0:
        print_parens(available_up, available_down - 1, height - 1, current_str + ")")
    
            
print_parens(3)
    