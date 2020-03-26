import nqueens as nq
from random import random, choice
import math

simulation_pairs = [[0.9, 1e-6], [0.75, 1e-7], [0.5, 1e-8]]
decay_queue = [0.9, 0.75, 0.5]
T_Thresh = [1e-6, 1e-7, 1e-8]
board_size = [4, 8, 16]

def schedule(T, decay_rate):
    return T * decay_rate

def print_initial_h(current):
    current.h = nq.numAttackingQueens(current)
    print("h-value =",current.h)

def simulatedAnnealing(current, thresh, decay):
    print('')

    T = 100
    loops = 0
    #main loop
    while (T >= thresh):
        current.h = nq.numAttackingQueens(current)

        if (current.h == 0):
            break

        children = nq.getSuccessorStates(current)
        child = choice(children)
        child.h = nq.numAttackingQueens(child)

        delta_h = current.h - child.h
        if (delta_h >= 0):
            current = child
        else:
            chance = math.e**(delta_h/T)
            if random() < chance:
                current = child

        ++loops

        T = schedule(T, decay)

    print("Result: Final board h-value =",current.h)
    current.printBoard()
    return current.h



def main():
    print('In main')
    run_count = 0

    for size in board_size:
        print("Board size:",size)
        for each in simulation_pairs:
            h_values = []
            print("Decay Rate =",each[0], "T Threshold =",each[1])
            print("\n")
            for x in range(0, 10):
                print("Run",x)
                startingBoard = nq.Board(size)
                startingBoard.rand()
                print("Initial Board:")
                startingBoard.printBoard()
                print_initial_h(startingBoard)
                temp = simulatedAnnealing(startingBoard, each[1], each[0])
                h_values.append(temp)
            print("Average h-value =",(sum(h_values) / len(h_values)))






if __name__ == "__main__":
    main()