#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    i = 0
    for line in matrix:
        squares.append(list(map(lambda x: x ** 2, line)))
        i += 1
    return squares;
        
