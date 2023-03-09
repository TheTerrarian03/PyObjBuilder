def getRectangleCornerCoordinates(size: tuple[int, int], pos: tuple[int, int]) -> list[tuple[int, int]]:
    '''Returns the coordinates of a rectangle's 4 corners
    
        Parameters
        ----------
            size : tuple
                Size of rectangle (x,y)
            pos : tuple
                Position of rectangle (x,y)
                
        Returns
        -------
            list[tuple[int, int]]
                a list of the coordinates, as tuples of 2 ints'''
    # order: top-left, top-right, bottom-left, bottom-right
    # size: (x-size, y-size)
    # pos: (x-pos from left, y-pos from top)
    corners = [(pos[0],         pos[1]),
               (pos[0]+size[0], pos[1]),
               (pos[0],         pos[1]+size[1]),
               (pos[0]+size[0], pos[1]+size[1])]
    return corners

def isWithinRange(min: float, max: float, current: float) -> bool:
    '''Returns a true/false based on whether the current value is within the min/max range'''
    if (min < current < max):
        return True
    return False

def isApproxAt(targetVal, currentVal, error):
    # check if value is within target in area of error (total area is double of error)
    if ((targetVal - error) < currentVal < (targetVal + error)):
        # approximately at value
        return True
    # not approximately at value
    return False

def isApproxAt2D(targetPoint, currentPoint, error):
    # first check x-position for approx
    if (isApproxAt(targetPoint[0], currentPoint[0], error)):
        # then check for y-position for approx
        if (isApproxAt(targetPoint[1], currentPoint[1], error)):
            # approximately at coordinate/position
            return True
    # not approximately at coordinate/position
    return False

def getApproxMousePos(size: tuple[int, int], pos: tuple[int, int], mousePos: tuple[int, int], error: int=2):
    rectCorners = getRectangleCornerCoordinates(size, pos)
    # first check all 4 corners- corners take priority
    if (isApproxAt2D(rectCorners[0], mousePos, error)):
        return "TL"
    if (isApproxAt2D(rectCorners[1], mousePos, error)):
        return "TR"
    if (isApproxAt2D(rectCorners[2], mousePos, error)):
        return "BL"
    if (isApproxAt2D(rectCorners[3], mousePos, error)):
        return "BR"
    # then, check for edges if mouse is not near any corners
    # check for x-val approx
    if (isApproxAt(pos[0], mousePos[0], error)):
        # check for within height of wall
        if (isWithinRange(pos[1], pos[1]+size[1], mousePos[1])):
            return "L"
    if (isApproxAt(pos[0]+size[0], mousePos[0], error)):
        if (isWithinRange(pos[1], pos[1]+size[1], mousePos[1])):
            return "R"
    # check for y-val
    if (isApproxAt(pos[1], mousePos[1], error)):
        if (isWithinRange(pos[0], pos[0]+size[0], mousePos[0])):
            return "T"
    if (isApproxAt(pos[1]+size[1], mousePos[1], error)):
        if (isWithinRange(pos[0], pos[0]+size[0], mousePos[0])):
            return "B"
    # if all else fails, return "NONE"
    return "NONE"