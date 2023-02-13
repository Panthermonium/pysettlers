import random
from TileResource import TileResource

def tiles():
        tiles = []

        for i in range(4):
            tiles.append(TileResource.Lumber)
            tiles.append(TileResource.Grain)
            tiles.append(TileResource.Wool)

            if i < 3:
                tiles.append(TileResource.Brick)
                tiles.append(TileResource.Ore)

            if i == 0:
                continue
        tiles.append(TileResource.Nothing)

        return tiles

def tileNum():
        tileNums = []
        for i in range(3, 12):
            if i == 7:
                continue
            else:
                tileNums.append(i)
                tileNums.append(i)
        tileNums.append(2)
        tileNums.append(12)
        tileNums.append(7)

        return tileNums



class Hex:
    def __init__(self, resource, roll):
        self.resource = resource
        self.roll = roll


hexRes = tiles()
hexNum = tileNum()

restest = random.sample(hexRes[:18],18)
restest.append(TileResource.Nothing)

def merge(list1, list2):
     
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


new_board = merge(restest,hexNum)

shuffle = random.sample(new_board, k=len(new_board))

map = {

}

for q in range(5):
    for r in range(5):
        map.update({(q,r) : ''})




map.update({(0,0): None})
map.update({(1,0): None})
map.update({(0,1): None})
map.update({(4,3): None})
map.update({(3,4): None})
map.update({(4,4): None})


for i in range(5):
        for j in range(5):
            if map.get((i,j)) != None:
                map.update({(i,j): Hex(shuffle[0][0],shuffle[0][1])})


print('')


print(map[(0,2)].resource)
print(map[(0,2)].roll)
