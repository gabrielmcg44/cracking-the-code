
import sys

def box_is_between(medium_box, small_box, large_box):
    return (
        medium_box[0] > small_box[0] and medium_box[0] < large_box[0] and
        medium_box[1] > small_box[1] and medium_box[1] < large_box[1] and
        medium_box[2] > small_box[2] and medium_box[2] < large_box[2]
    )

def get_added_stack(new_box, stack):
    stack_size = len(stack)
    new_stack = []
    added_stack = False
    for i in range(stack_size):
        previous_box = None
        next_box = None
        if stack[i][1] > new_box[1] and not added_stack:
            previous_box = [0]*3 if i == 0 else stack[i-1]
            next_box = stack[i]
            if box_is_between(new_box, previous_box, next_box):
                new_stack.append(new_box)
                added_stack = True
            else:
                return None
                
        new_stack.append(stack[i]) 
              
        if i == stack_size - 1 and stack[i][1] <= new_box[1]:
            previous_box = stack[i]
            next_box = [sys.maxsize]*3
            if box_is_between(new_box, previous_box, next_box):
                new_stack.append(new_box)
            else:
                return None
            
    return new_stack

def get_stacks(boxes):
    stacks = []
    shorter_box = boxes[0] 
    stacks.append([shorter_box])
    if len(boxes) == 1:
        return stacks
        
    stacks_without_first = get_stacks(boxes[1:])
    
    for stack in stacks_without_first:
        stacks.append(stack)
        new_stack = get_added_stack(shorter_box, stack)
        if new_stack is not None:
            stacks.append(new_stack)
           
    return stacks

def tallest_stack_height(boxes):
    return max([ sum([box[1] for box in stack]) for stack in get_stacks(boxes) ])


boxes = [
    [ 6, 5, 3 ],
    [ 8, 6, 6 ],
    [ 13, 12, 15 ],
    [ 11, 11, 2 ], 
    [ 2, 8, 5 ],
    [ 9, 12, 14 ],
    [ 1, 2, 3 ],
    [ 2, 4, 3 ],
    [ 5, 4, 7 ],
    [ 12, 6, 8 ],
    [ 4, 9, 11 ],
    [ 12, 14, 4 ]
]

for stack in get_stacks(boxes):
    print(stack)

print(tallest_stack_height(boxes))


