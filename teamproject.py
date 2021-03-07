class MCBState:
    def __init__(objects, stateV, numberM=0, parent=None):
        objects.stateV = stateV
        objects.numberM = numberM
        objects.parent = parent
        
    @classmethod
    def root(cls):
        return cls((3,3,1))
# Missionaries, Cannibals, Boat
    def possibleMoves(objects):

        moves = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]
        return moves
# Max allowable number of these objects moved in a single move combined equals 2

    def allowable(objects):
        missionaries = objects.stateV[0]
        cannibals = objects.stateV[1]
        if missionaries > 3 or missionaries < 0: 
            return False
        elif cannibals > 3 or cannibals < 0:
            return False
        return True
# To prevent forbidden possibilities such as (4,2,1) from occuring

    def solution(objects):
        if objects.stateV == (0,0,0):
            return True
        return False
# Goal State

    def unallowable(objects):
        missionaries = objects.stateV[0]
        cannibals = objects.stateV[1]
        boat = objects.stateV[2]
        if missionaries > 0 and missionaries < cannibals:
            return True
        if 3 - missionaries > 0 and 3 - missionaries < 3 - cannibals:
            return True
        return False
# Cannibals can not outnumber missionaries on any side, if missionaries are present there

    def nextStates(objects):
        moves = objects.possibleMoves()
        states = list()
        missionariesRight, cannibalsRight, boatRight = objects.stateV
        for move in moves:
            altermissionaries, altercannibals = move
            if boatRight == 1:  
                newstateV = (missionariesRight-altermissionaries, cannibalsRight-altercannibals, 0)
            else:
                newstateV = (missionariesRight+altermissionaries, cannibalsRight+altercannibals, 1)
# Add to move right and subtract to move left
            newState = MCBState(newstateV, objects.numberM+1, objects)
            if newState.allowable():
                states.append(newState)

        return states

    def __str__(objects):
        return "MCBState[{}]".format(objects.stateV)

    def __repr__(objects):
        return str(objects)

# Performing the search    
def search(dfs=True):
    
    from collections import deque
    
    root = MCBState.root()
    
    search = deque()
    
    statesSeen = set()
    
    solutions = list()
    
    search.append(root)
    
    loopCount = 0
    maxLoop = 10000
    
    while len(search) > 0:
        loopCount += 1
        if loopCount > maxLoop:
            print(len(search))
            break
    
        currentState = search.pop()

        nextStates = currentState.nextStates()

        for possiblenextState in nextStates[::-1]:
            
            possiblestateV = possiblenextState.stateV
            
            if possiblestateV not in statesSeen:
                
                if possiblenextState.unallowable():
                    continue
                elif possiblenextState.solution(): 
                    solutions.append(possiblenextState)
                    continue
                    
                if dfs:
                    search.append(possiblenextState)
                else:
                    search.appendleft(possiblenextState)

                statesSeen.add(possiblestateV)
                
    print("{} solutions found".format(len(solutions)))
    return solutions

solDfs = search(True)
solBfs = search(False)

print(".......BFS.........")
currentState = solBfs[0]
while currentState:
    print(currentState)
    currentState = currentState.parent    
        
print(".......BFS.........")
currentState = solBfs[1]
while currentState:
    print(currentState)
    currentState = currentState.parent
        
print(".......DFS.........")
currentState = solDfs[0]
while currentState:
    print(currentState)
    currentState = currentState.parent
    
print(".......DFS.........")
currentState = solDfs[1]
while currentState:
    print(currentState)
    currentState = currentState.parent
