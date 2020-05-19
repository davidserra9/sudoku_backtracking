# Author: David Serrano
# github: davidserra9

def solve(matrix):
    """
    This function is in charge of solving the sudoku with
    the backtracking algorithm
    First, find the next empty blank space
    Secondly, try every value from 1 to 10 and validate it.
    Then call iteratively the function solve which if it finds
    finds a bad possibility will go back. 
    """
    blank = find_next_empty(matrix)
    if blank:
        row, col = blank
    else:
        return True

    for i in range(1,10):
        if validation(matrix,(row,col), i):
            matrix[row][col] = i
            if solve(matrix):
                return True
            
            matrix[row][col] = 0
    return False


def find_next_empty(matrix):
    """
    This function is in charge of finding the next
    empty position (0 in our case) of the matrix, going 
    first horizontally and then vertically.
    We return the position or None if there are not empty
    positions.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return (i,j)
    return None

def validation(matrix, position, num):
    """
    This function is in charge of finding if the number num
    is valid in the position position.
    First, check the row.
    Second, check the column
    Third, check the box 
    """
    for i in range(0, len(matrix)):
        if matrix[position[0]][i] == num and position[1] != i:
            return False
    
    for i in range(0,len(matrix[0])):
        if matrix[i][position[1]] == num and position[0] != i:
            return False

    """
    To evaluate the box we have to firstly know in which box is 
    the position, and then look the value in each position
    """

    box_hor = position[0] // 3
    box_ver = position[1] // 3

    for i in range (0,3):
        for j in range (0,3):
            if matrix[3*box_hor + i][3*box_ver + j] == num and (3*box_hor + i, 3*box_ver + j) != position:
                return False
    
    return True

def print_matrix(matrix):
    """
    This function is in charge of printing the final result
    of the sudoku in an easy way 
    """
    for i in range (len(matrix)):
        if i % 3 == 0:
           print(" ----------------------")

        for j in range (len(matrix[0])):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(matrix[i][j], end=" |\n")          
            else:
                print(matrix[i][j], end=" ")
    
    print(" ----------------------")

"""
empty sudoku to solve where 0 mean blank spaces
"""
matrix = [
        [0,3,6,7,0,9,0,1,5],
        [0,5,0,1,0,4,0,0,0],
        [4,1,2,0,0,0,0,0,0],
        [6,0,0,2,7,3,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,4,8,5,0,0,1],
        [0,0,0,0,0,0,2,4,8],
        [0,0,0,9,0,8,0,5,0],
        [1,8,0,5,0,2,6,3,0]
]

#pp = pprint.PrettyPrinter(width = 41, compact=True)      
solve(matrix)
#pp.pprint(matrix)
print("stop")
print_matrix(matrix)          




