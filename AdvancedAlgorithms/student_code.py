import math


# A helper function to calculate the Euclidean, Manhattan, and Diagonal distance between two points
# This heuristic is admissable as it cannot over-estimate the distance between points
def heuristic(point1, point2, heuristic_type="euclidean"):
    if heuristic_type == "manhattan":
        # Manhattan distance
        return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    elif heuristic_type == "diagonal":
        # Diagonal distance
        dx = abs(point2[0] - point1[0])
        dy = abs(point2[1] - point1[1])
        return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)
    else:
        # Default to Euclidean distance
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def shortest_path(M, start, goal, heuristic_type="euclidean"):
    """
    Main idea: expand based on f = g + h, where
    g: path cost from start to current node
    h: heuristic estimate of distance from current node to goal
    """
    # Initialize data structures
    # Use sets for efficient insertion and lookup
    open_set = {start}
    closed_set = set()
    g_score = {start: 0}
    f_score = {start: 0 + heuristic(M.intersections[start], M.intersections[goal], heuristic_type)}
    previous = {}

    while open_set:
        # Select the node with the lowest f_score = g_score + h_score (heuristic)
        current = min(open_set, key=lambda x: f_score[x])

        if current == goal:
            # Goal reached, reconstruct the path
            path = [current]
            while current in previous:
                current = previous[current]
                path.append(current)
            path.reverse()
            return path

        # Move current node from open set to closed set
        open_set.remove(current)
        closed_set.add(current)

        # Expand the current node's neighbors
        for neighbor in M.roads[current]:
            if neighbor in closed_set:
                continue

            # Calculate the tentative g_score for the neighbor
            tentative_g_score = g_score[current] + heuristic(M.intersections[current], M.intersections[neighbor], heuristic_type)

            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                # Update the g_score, f_score, and previous node
                g_score[neighbor] = tentative_g_score
                # f = g + h
                f_score[neighbor] = g_score[neighbor] + heuristic(M.intersections[neighbor], M.intersections[goal], heuristic_type)
                previous[neighbor] = current

                if neighbor not in open_set:
                    # Add neighbor to the open set
                    open_set.add(neighbor)

    # No path found
    return None
