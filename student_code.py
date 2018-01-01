from math import sqrt
import sys

def shortest_path(M,start,goal):
    print("shortest path called")
    expanded = set()
    frontier = set([start])
    g_cost = {start:0} # cost from origin, without heuristic
    g_predecessor = {start:None}
    while frontier:
        # Choose best node from frontier
        best_node, best_cost = None, sys.maxsize
        for node in frontier:
            node_cost = g_cost[node]+h_function(node, goal, M.intersections)
            if node_cost < best_cost:
                best_cost = node_cost
                best_node = node
        
        if best_node == None:
            break

        # Choose best_node and expand it
        frontier.remove(best_node)
        expanded.add(best_node)
        
        if best_node == goal:
            continue
        
        # Update expanded nodes costs coming from best_node
        expansion = M.roads[best_node]
        for node in expansion:
            node_cost = g_cost[best_node] + distance(M.intersections[best_node], M.intersections[node])
            if node not in expanded:
                if node not in frontier:
                    frontier.add(node)
                    g_cost[node] = node_cost
                    g_predecessor[node] = best_node
                elif node_cost < g_cost[node]:
                    g_cost[node] = node_cost
                    g_predecessor[node] = best_node

        #print("- ", best_node, best_cost, expansion, g_cost, g_predecessor)
    
    # Get the solution
    result = []
    node = goal
    while node != None:
        result.insert(0, node)
        node = g_predecessor[node] # predecessor

    return result

def h_function(current, goal, coords):
    """ Heuristic. Distance from current to goal. """
    return distance(coords[current], coords[goal])

def distance(node1, node2):
    x2, y2 = node2[0], node2[1]
    x1, y1 = node1[0], node1[1]
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )