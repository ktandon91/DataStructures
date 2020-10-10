# A common approach is to convert grids to a familiar format
# adjancy matrix/list

def get_sparse_matrix(r,c,val):
    matrix = [[val for j in range(c)] for i in range(r) ]
    return matrix

# we can directly run the algo on grid and we do not have to transform it to any adjancy matrix/list
# to traverse the neighbouring/adjacent cells of a grid we can manipulate r, c coordinate to get a value.


########ACCESSING GRID #############


#Define the direction vectors for
#north, south, east, west

# dr = [-1,1,0,0]
# dc = [0,0,1,-1]
#
# for i in range(len(dc)):
#     rr = r + dr[i]
#     cc = c + dr[i]
#
#     #skip invalid cells. Assume R and
#     #C for the number of rows and columns
#
#     if rr < 0 or cc <0: continue
#     if rr >=R or cc >=C: continue
#     #(rr, cc) is a neighbouring cell of (r,c)

#############PSEUDO CODE ###################

def solve_dungeon(R,C, input_grid, sr, sc):
    """
    :param R: rows of an input grid
    :param C: columns of an input grid
    :param input_grid: actual input grid with . denoting path, E denoting exit, # denoting no path
    :param sc: starting column coordinate
    :param rc:  starting row coordinate
    :return:
    """
    #### Initializate visited matrix, to keep track if a grid is visited or not it will be of same size, R and C
    visited = get_sparse_matrix(R,C, False)

    ### initialize rq, rc -- to enque r and column coordinates for bfs
    rq, cq = [], []

    ###### Initialize variables to track the number of steps taken
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    ### variabl to keep track if end "E" is ever reached.
    reached_end = False

    # Define the direction vectors for
    # north, south, east, west
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]

    ####Solving Algo#######
    ## enque starting cooordinates
    ## mark the starting coordinates as visited
    ## Repeat while queue is not empty
    ## Take first element out and start processing it

    rq.append(sr)
    cq.append(sc)

    visited[sr][sc] = True

    while rq:
        r, c = rq.pop(0), cq.pop(0)


        if input_grid[r][c] == 'E':
            reached_end = True
            break

        explore_neighbours(r,c,R,C,input_grid, visited, rq,cq, dr,dc, nodes_in_next_layer)

        #nodes left in layer and nodes in next layer have literal meaning in algo

        nodes_left_in_layer -=1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1

    if reached_end:
        return move_count

    return -1

def explore_neighbours(r,c,R,C,input_grid, visited, rq,cq, dr,dc, nodes_in_next_layer):
    ## explore the neigboring coordinates

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        ## Skip out of bounds locations
        if rr <0 or cc <0: continue
        if rr >=R or cc >=C: continue

        #skip visited and blocked locations
        if visited[rr][cc] or input_grid[rr][cc] == '#':
            continue

        rq.append(rr)
        cq.append(cc)

        visited[rr][cc] = True
        nodes_in_next_layer+=1


solve_dungeon(10,5,[[1,2,3],[2,3,4]],0,0)