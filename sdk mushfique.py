import numpy as np
import copy
import math
import time


def check_master(row,column,grid_master):
    if grid_master[row][column] == 0:
        print ("No conflict with master grid.")
        return 0
    print("Conflict with master grid.")
    return 1

def check_cell(row, column, guess,grid_working):

    column_check = []
    for i in range(9):
        column_check.append(grid_working[i][column])

    row_quadrant = math.floor(row / 3) + 1
    column_quadrant = math.floor(column / 3) + 1

    quadrant = []

    for i in range(3):
        for j in range(3):
            x = (row_quadrant * 3) -3 + i
            y = (column_quadrant * 3) - 3 + j
            w = grid_working[x][y]
            quadrant.append(w)

    if guess in column_check:
        print ("Column conflict")
        return 1

    elif guess in grid_working[row]:
        print ("Row conflict.")
        return 1

    elif guess in quadrant:
        print ("Quadrant conflict.")
        return 1

    else:
        print ("Row, column and quadrant clear.")
        return 0
def sdk3_main(grid_master):
    grid_working = copy.deepcopy(grid_master)
    print ("Initial")
    print (np.matrix(grid_working))
    print()

    cell = 0
    movement = 1
    count = 0

    while cell < 81:

        count +=1
        print("Count: ", count)

        # time.sleep(0.005)

        row = math.floor(cell/9)
        column = cell % 9
        print(cell,": [",row, column,"]")

        x = check_master(row, column,grid_master)
        print("Cell movement: ", movement)
        if x == 1:
            cell += movement

        else:
            if movement == 1:

                guess = 1

                while guess < 10:
                    print("Guess: ",guess)
                    x = check_cell(row, column, guess,grid_working)
                    if x == 1:
                        guess += 1
                    else:
                        break

                if guess == 10:
                    print("Nothing works, try going back a cell ...")
                    cell -= 1
                    movement = -1

                else:
                    grid_working[row][column] = guess
                    print ("Looks good!")
                    cell += 1

            else: ### movement = -1

                guess = grid_working[row][column] + 1

                while guess < 10:
                    print ("Guess: ", guess)
                    y = check_cell(row, column, guess,grid_working)

                    if y == 1:
                        guess += 1

                    else:
                        break

                if guess == 10:
                    print ("Nothing works, need to go down another ... ")
                    grid_working[row][column] = 0
                    cell -= 1

                else:
                    grid_working[row][column] = guess
                    print ("Looks good, head back up ... ")
                    cell += 1
                    movement = 1


        print(np.matrix(grid_working))
        print()
