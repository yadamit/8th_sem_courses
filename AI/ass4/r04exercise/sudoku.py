#!/usr/bin/python3

from logic import AND, OR, NOT, ATOM

######### Cardinality constraints #########

def atLeast1(fmas):
  return OR(fmas)

def allpairs(lst): # Helper function for atMost1
  return [ (lst[i],lst[j]) for i in range(0,len(lst)) for j in range(i+1,len(lst)) ]

def atMost1(fmas):
    lst = allpairs(fmas)
    return AND([NOT(AND(list(f))) for f in lst])

def exactly1(fmas):
    return AND([atLeast1(fmas), atMost1(fmas)])

######### Translation of Sudoku to propositional logic #########

# Create atom from (x,y,n)
def nameS(c,r,n):
    return "S" + str(c) + "," + str(r) + "," + str(n)
def S(c,r,n):
    return ATOM("S" + str(c) + "," + str(r) + "," + str(n))

# Map 9X9 Sudoku instances to propositional formulas
#
# In formulas C1 to C4 below, instead of exactly1 it would be logically
# equivalent to use OR. However, the exactly1 allows Unit Propagation in DPLL
# to infer far more new literals, and cutting down the size of the search tree
# to a small fraction. In fact, our simple SAT solver needs at least a couple
# of hours (and possibly far far longer: these runs did not finish before we
# terminated them after 2 hours) to solve even simple instances if there is
# OR instead of exactly1 in these formulas.

def sudoku2fma(puzzle):

    # Every grid cell has exactly one value
    C1 = AND([ exactly1([ S(c,r,n) for n in range(1,10) ]) for r in range(1,10) for c in range(1,10) ])

    # Every row has all numbers
    C2 = AND([ exactly1([ S(c,r,n) for c in range(1,10) ]) for r in range(1,10) for n in range(1,10) ])
    
    # Every column has all numbers
    C3 = AND([ exactly1([ S(c,r,n) for r in range(1,10) ]) for c in range(1,10) for n in range(1,10) ])

    # Every 3X3 sub-grid has all numbers
    C4 = []
    for n in range(1,10):
        for x in range(1,10,3):
            for y in range(1,10,3):
                C4 += [ exactly1( [S(x+i, y+j, n) for i in range(3) for j in range(3)] )]
    C4 = AND(C4)
    
    # The solution respects the given clues
    C5 = AND([ S(x,y,n) for (x,y,n) in puzzle ])

    return AND([C1,C2,C3,C4,C5])

  
### Output a satisfying valuation for Sudoku as a 9X9 grid

def showsudokuclues(clues):
    for y in range(9,0,-1):
        for x in range(1,10):
            flag = False
            for n in range(1,10):
                if (x,y,n) in clues:
                    print(str(n),end='')
                    flag = True
            if not flag:
                print(".",end='')
            if x in [3,6]:
                print("|",end='')
        print("")
        if y in [7,4]:
            print("===|===|===")

def showsudoku(V):
    for y in range(9,0,-1):
        for x in range(1,10):
            for n in range(1,10):
                if V[nameS(x,y,n)]:
                    print(str(n),end='')
            if x in [3,6]:
                print("|",end='')
        print("")
        if y in [7,4]:
            print("-----------")
