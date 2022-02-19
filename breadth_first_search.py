'''solve 2d and 3d array with BFS'''


class BreadthSearch:
    '''base class for breadth search'''

    final_state = [1, 2, 3, 0]
    dims = 2
    frontier_stack = []
    traversed_nodes = []

    def __init__(self, initial_state):
            self.initial_state = initial_state
            if len(initial_state) == 9:
                self.final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
                self.dims = 3

    def breadth_search(self):
        '''start the breadth search of the puzzle'''
        if self.dims == 2:
            self.search_2d()
        else:
            self.search_3d()
    

    def search_2d(self):
        '''search the states of the 2d puzzle to find the answer'''
        current_state = self.initial_state
        self.traversed_nodes.append(current_state)
        self.find_possible_states(current_state) #pushes possible states into frontier stack
        while current_state != self.final_state:
          if self.frontier_stack == []:
              print("This is not solvable")
              break
          current_state =  self.frontier_stack[0]
          self.frontier_stack.pop(0)
          self.traversed_nodes.append(current_state)
          self.find_possible_states(current_state)
        print("The path traversed is: " + str(self.traversed_nodes))




    def search_3d(self):
        '''search the states of the 3d puzzle to find the answer'''
        current_state = self.initial_state
        self.traversed_nodes.append(current_state)
        self.find_possible_states(current_state) #pushes possible states into frontier stack
        while current_state != self.final_state:
            if self.frontier_stack == []:
                break
            current_state =  self.frontier_stack[0]
            self.frontier_stack.pop(0)
            self.traversed_nodes.append(current_state)
            self.find_possible_states(current_state)
        print("The path traversed is: " + str(self.traversed_nodes))
        if self.frontier_stack == []:
            print("This is not solvable")

    def find_possible_states(self, given_state):
        '''find all possible movements from the current state and add to frontier stack'''
        state_matrix = [[given_state[0], given_state[1]], [given_state[2], given_state[3]]]
        if self.dims == 3:
            state_matrix = [   [ given_state[0], given_state[1], given_state[2] ],   
                                [ given_state[3], given_state[4], given_state[5] ],    
                                [ given_state[6], given_state[7], given_state[8] ]    ]

        for row in range(self.dims):
            for col in range(self.dims):
                below = row+1
                if below < self.dims: 
                    if state_matrix[below][col] == 0:
                        possible_state = swap_position(state_matrix, row, col, below, col)
                        if possible_state not in self.traversed_nodes:
                            self.frontier_stack.append(possible_state)
                above = row-1
                if above >= 0:
                    if state_matrix[above][col] == 0:
                        possible_state = swap_position(state_matrix, row, col, above, col)
                        if possible_state not in self.traversed_nodes:
                            self.frontier_stack.append(possible_state)
                right = col + 1
                if right < self.dims:
                    if state_matrix[row][right] == 0:
                        possible_state = swap_position(state_matrix, row, col, row, right)
                        if possible_state not in self.traversed_nodes:
                            self.frontier_stack.append(possible_state)                           
                left = col - 1
                if left >= 0:
                    if state_matrix[row][left] == 0:
                        possible_state = swap_position(state_matrix, row, col, row, left)
                        if possible_state not in self.traversed_nodes:
                            self.frontier_stack.append(possible_state)



def swap_position(matrix, row, col, new_row, new_col):
    matrix_1d, dim = translate2d_1d(matrix)
    matrix_1d[(row * dim) + col], matrix_1d[(new_row * dim) + new_col] = matrix_1d[(new_row * dim) + new_col], matrix_1d[(row * dim) + col]
    return matrix_1d

def translate2d_1d(matrix):
    one_dim = []
    dim = len(matrix)
    for row in range(dim):
        for col in range(dim):
            one_dim.append(matrix[row][col])
            #print(str(row) + " " + str(col))
    return one_dim, dim



                    


        
