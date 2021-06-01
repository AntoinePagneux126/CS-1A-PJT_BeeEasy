import numpy as np

def compute_box(box1, box2):
    return [min(box1[0], box2[0]), min(box1[1], box2[1]), max(box1[2], box2[2]), max(box1[3], box2[3])]

def distance(point1, point2):
    return (point1[0] - point2[0]) * (point1[0] - point2[0]) + (point1[1] - point2[1]) * (point1[1] - point2[1])

def distance_box(, box1, box2):
    mid_box1 = [(box1[0]+box1[2])/2, (box1[1]+box1[3])/2]
    mid_box2 = [(box2[0]+box2[2])/2, (box2[1]+box2[3])/2]
    return distance(mid_box1, mid_box2)

def localization_correction(loc, threshold):
    dist = [[distance_box(loc[i], loc[j])  < threshold for j in range(len(loc))] for i in range(len(loc))]
    added = [False] * len(loc)
    bb = []
    for i in range(len(loc)):
        if not added[i]:
            new_box = loc[i]
            for j in range(i+1, len(loc)):
                if dist[i][j]:
                    new_box = compute_box(new_box, loc[j])
                    added[j] = True
            bb.append(new_box)
    return bb

def DFS(img, i, j):

    visited = {}
    next_node = []

    next_node.append((i, j))
    visited[(i, j)] = True

    connected = []

    while(len(next_node) != 0):

        n = next_node.pop()
        connected.append(n[0]*.shape[1]+n[1])

        for x in range(n[0]-1 if n[0] > 0 else 0, n[0]+2 if n[0] < .shape[0]-1 else .shape[0]):
            for y in range(n[1]-1 if n[1] > 0 else 0, n[1]+2 if n[1] < .shape[1]-1 else .shape[1]):
                if((x, y) in visited):
                    continue
                else:
                    if(img[x, y] == 1):
                        next_node.append((x, y))
                        visited[(x, y)] = True
    return connected

def compute_frame(img):
    img = np.array(img, dtype=np.int32)
    shape = img.shape
    visited = [False for _ in range(shape[0]*shape[1])]
    localization = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if(visited[i*shape[1]+j] == False):
                if(img[i, j] == 0):
                    visited[i*shape[1]+j] = True
                else:
                    connected = DFS(img, i, j)
                    x1 = shape[0]
                    y1 = shape[1]
                    x2 = y2 = 0
                    for point in connected:
                        visited[point]  = True
                        if len(connected) > threshold:
                            x, y = point // shape[1], point % shape[1]
                            noise_free[x, y] = 1
                            x1 = min(x1, x)
                            y1 = min(y1, y)
                            x2 = max(x2, x)
                            y2 = max(y2, y)
                    if len(connected) > 5:
                        localization.append([x1, y1, x2, y2])
    return localization_correction(localization)
