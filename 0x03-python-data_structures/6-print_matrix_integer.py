#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for z in range(len(matrix[x])):
            if z != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][z]), end='')
        print()
