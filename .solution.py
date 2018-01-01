from math import sqrt

def shortest_path(M, start, goal):
    """
    A* search Implementation.
    
    Returns the lowest cost path from start to goal.
    """
    
    pos = M.intersections
    M = M.roads
    
    closed = set()
    opened = set([start])
    came_from = {}
    num_nodes = len(M)
    g_scores = [99999 for _ in range(num_nodes)]
    f_scores = [99999 for _ in range(num_nodes)]
    g_scores[start] = 0.0
    f_scores[start] = heuristic(start, goal, pos)
    
    while opened:
        current = get_next_node(opened, f_scores)
        if current == goal:
            print("f_score:", f_scores[current])
            print("g_score:", g_scores[current])
            return reconstruct_path(came_from, current, start)
        opened.remove(current)
        closed.add(current)
        neighbors = M[current]
        for neighbor in neighbors:
            if neighbor in closed:
                continue
            if neighbor not in opened:
                opened.add(neighbor)
            
            tentative_g = g_scores[current] + distance(current, neighbor, pos)
            if tentative_g >= g_scores[neighbor]:
                continue
            came_from[neighbor] = current
            g_scores[neighbor] = tentative_g
            f_scores[neighbor] = g_scores[neighbor] + heuristic(neighbor, goal, pos)
    return None

def get_next_node(opened, f_scores):
    best_idx = None
    lowest_f = 9999999
    for node in opened:
        f = f_scores[node]
        if f < lowest_f:
            best_idx = node
            lowest_f = f
    return best_idx

def reconstruct_path(came_from, current, start):
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
    
    
def distance(start, goal, pos):
    x1, y1 = pos[start]
    x2, y2 = pos[goal]
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

def heuristic(start,goal,pos):
    return distance(start, goal, pos)