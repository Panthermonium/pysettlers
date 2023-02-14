import random
from Tile import *
class Board:
    def __init__(self) -> None:
        pass


def generateResources():
    resources = []

    for i in range(4):        #4 times
        resources.append(TileResource.Lumber)
        resources.append(TileResource.Grain)
        resources.append(TileResource.Wool)

    for i in range(3):            #3 times
        resources.append(TileResource.Brick)
        resources.append(TileResource.Ore)

    resources.append(TileResource.Nothing)

    return resources

def generateNumTokens():
        numTokens = []
        for i in range(3, 12):
            if i == 7:
                continue
            else:
                numTokens.append(i)
                numTokens.append(i)
        numTokens.append(2)
        numTokens.append(12)
        numTokens.append(7)

        return numTokens

def merge_list(list1, list2):
     
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def generateTileData():
    merged_data = merge_list(generateResources(),generateNumTokens())
    shuffled_tiles = random.sample(merged_data, k=len(merged_data))

    return shuffled_tiles

def createHexGrid():
    grid = {}
    for q in range(5):
        for r in range(5):
            grid.update({(q,r) : ''})
#update map with null tiles
    grid.update({(0,0): None})
    grid.update({(1,0): None})
    grid.update({(0,1): None})
    grid.update({(4,3): None})
    grid.update({(3,4): None})
    grid.update({(4,4): None})

    return grid

def setupBoard(tiledata):
    grid = createHexGrid()
    tiles = tiledata
    num = 0
    for i in range(5):
        for j in range(5):
            if grid.get((i,j)) != None:
                grid.update({(i,j): Tile(*tiledata.pop())})
                num = num + 1

                    
    
    return grid

testboard = setupBoard(generateTileData())



print(testboard[(1,1)].__dict__)

print(testboard.values())

test = []

for val in testboard.values():
    test.append(val)

count  = 0
for i in test:
    if i != None:
        print(i.__dict__)
        count  = count + 1

print(count)