import numpy as np

def distance_point(point1, point2):
    return (point1[0] - point2[0]) * (point1[0] - point2[0]) + (point1[1] - point2[1]) * (point1[1] - point2[1])

def distance_box(box1, box2):
    mid_box1 = [(box1[0]+box1[2])/2, (box1[1]+box1[3])/2]
    mid_box2 = [(box2[0]+box2[2])/2, (box2[1]+box2[3])/2]
    return distance_point(mid_box1, mid_box2)

def distance_boxes(boxes1, boxes2, threshold):
    n1 = len(boxes1)
    n2 = len(boxes2)
    couple = []
    for i in range(n1):
        minimum = distance_box(boxes1[i], boxes2[0])
        index = 0
        for j in range(n2):
            if (x := distance_box(boxes1[i], boxes2[j])) < minimum:
                minimum = x
                index = j
        if minimum < threshold:
            couple.append([i, j])
    return couple

def travel(couple, l_couples):
    next_elt = couple[1]
    found = True
    target = 0
    while found:
        for i in range(len(l_couples[target])):
            if l_couples[target][i][0] == next_elt:
                next_elt = l_couples[target][i][1]
                del l_couples[target][i]
                target += 1
                break
        else:
            found = False
    return target + 1

def time_elapsed(bounding_boxes, dt, threshold, MaxTime):
    couples = []
    n = len(bounding_boxes)
    frelon_detected = []
    for i in range(n-1):
        couples.append(distance_boxes(bounding_boxes[i], bounding_boxes[i+1], threshold))
    for i in range(n-1):
        n1 = len(couples[i])
        for j in range(n1):
            couple = couples[i][j]
            link = travel(couple, couples[i+1:])
            if link * dt > MaxTime:
                frelon_detected.append(i)
    return frelon_detected
