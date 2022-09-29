   
def is_between(mid, edge1, edge2):
    return (edge1 - mid)*(edge2 - mid) <= 0
    
def colinear_intersection(min1, max1, min2, max2):
    if max2 >= max1 and min2 <= min1:
        return [min1, max1]
    elif max1 >= max2 and min1 <= min2:
        return [min2, max2]
    elif is_between(min1, min2, max2):
        return [min1, max2]
    elif is_between(min2, min1, max1):
        return [min2, max1]
    
    return -1

def intersection(point_a1, point_b1, point_a2, point_b2):
    
    x_diff1 = point_b1[0] - point_a1[0]
    y_diff1 = point_b1[1] - point_a1[1]
    x_diff2 = point_b2[0] - point_a2[0]
    y_diff2 = point_b2[1] - point_a2[1]
    
    if x_diff1 != 0 and x_diff2 != 0:
        slope1 = y_diff1 / x_diff1
        slope2 = y_diff2 / x_diff2
        const1 =  point_a1[1] - slope1 * point_a1[0]
        const2 =  point_a2[1] - slope2 * point_a2[0]
        if slope1 == slope2:
            if const1 == const2:
                x_points = colinear_intersection(
                    min([point_a1[1], point_b1[1]]), 
                    max([point_a1[1], point_b1[1]]), 
                    min([point_a2[1], point_b2[1]]), 
                    max([point_a2[1], point_b2[1]])
                )
                
                if x_points == -1:
                    return -1
                
                crossing = [[x_points[0], slope1*x_points[0] + const1], [x_points[1], slope1*x_points[1] + const1]]
                if crossing[0][0] == crossing[1][0]:
                    return crossing[0]
                
                return crossing
                
            return -1
        else:
            crossing = [(const2 - const1)/(slope1 - slope2), (slope1*const2 - slope2*const1)/(slope1 - slope2)]
            if is_between(crossing[0], point_b1[0], point_a1[0]) and is_between(crossing[0], point_b2[0], point_a2[0]):
                return crossing
                
            return -1
        
    elif x_diff1 != 0:
        slope1 = y_diff1 / x_diff1
        const1 =  point_a1[1] - slope1 * point_a1[0]
        if is_between(point_b2[0], point_a1[0], point_b1[0]) and is_between(slope1*point_b2[0] + const1, point_a2[1], point_b2[1]):
            return [point_b2[0], slope1*point_b2[0] + const1]
    
    elif x_diff2 != 0:
        slope2 = y_diff2 / x_diff2
        const2 =  point_a2[1] - slope2 * point_a2[0]
        if is_between(point_b1[0], point_a2[0], point_b2[0]) and is_between(slope2*point_b1[0] + const2, point_a1[1], point_b1[1]):
            return [point_b1[0], slope2*point_b1[0] + const2]
    
    elif point_b1[0] == point_b2[0]:
        y_points = colinear_intersection(
            min([point_a1[1], point_b1[1]]), 
            max([point_a1[1], point_b1[1]]), 
            min([point_a2[1], point_b2[1]]), 
            max([point_a2[1], point_b2[1]])
        )
        
        if y_points == -1:
            return -1
        
        crossing = [ [point_b1[0], y_points[0]], [point_b1[0], y_points[1]] ]

        if crossing[0][1] == crossing[1][1]:
            return crossing[0]
        
        return crossing
    
    return -1  


point_a1 = [0, 0]
point_b1 = [1, 2.1]

point_a2 = [0.5, 0]
point_b2 = [0.5, 1]

crossing = intersection(point_a1, point_b1, point_a2, point_b2)
print(crossing)