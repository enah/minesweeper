import random

def stepon(x, y, swept, adjacent):
    if x < 0 or y < 0 or x >= len(swept[0]) or y >= len(swept):
        return
    if swept[y][x] == True:
        return
    swept[y][x] = True
    if adjacent[y][x] == 0:
        for diffy in [-1, 0, 1]:
            for diffx in [-1, 0, 1]:
                stepon(x + diffx, y + diffy, swept, adjacent)
                
def wincondition(mines, swept):
    for j in range(len(swept)):
        for i in range(len(swept[0])):
            if not mines[j][i] and not swept[j][i]:
                return False
    return True

def minesweeper(n, m):
    mines = []
    for j in range(m):
        mines.append([random.random() > 0.85 for i in range(n)])
    swept = []
    for j in range(m):
        swept.append([False for i in range(n)])
    adjacent = []
    for j in range(m):
        adjacent.append([0 for i in range(n)])
    for j in range(m):
        for i in range(n):
            countmines = 0
            for diffj in [-1, 0, 1]:
                for diffi in [-1, 0, 1]:
                    countj = j + diffj
                    counti = i + diffi
                    if countj >= 0 and counti >= 0 and countj < m and counti < n:
                        countmines += mines[countj][counti]
            adjacent[j][i] = countmines
    
    while True:
        for j in range(m):
            print(" ".join([str(adjacent[j][i]) if swept[j][i] else "X" for i in range(n)]))
        s = raw_input() # X Y
        x, y = [int(i) for i in s.split()]
        if x < 0 or y < 0 or x >= n or y >= m:
            print("Out of bounds. Enter again")
            continue
        if mines[y][x]:
            print("Stepped on a mine! Game over")
            break
        stepon(x, y, swept, adjacent)
        if wincondition(mines, swept):
            print("You win!")
            for j in range(m):
                print(" ".join([str(adjacent[j][i]) if swept[j][i] else "X" for i in range(n)]))
            break
