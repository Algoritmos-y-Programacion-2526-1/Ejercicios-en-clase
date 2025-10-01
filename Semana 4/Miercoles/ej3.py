def validate_point(path):
    path_list = [(0,0)]
    x,y = 0,0
    for position in path:
        if position == "N":
            y +=1
        elif position == "S":
            y -=1
        elif position == "E":
            x +=1
        elif position == "W":
            x -=1
        if (x,y) in path_list:
            return True
        else:
            path_list.append((x,y))
    return False
    
        

print(validate_point("NESWW"))