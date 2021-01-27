import json

# 已经遍历过的坐标
coordinateHasTraversed = []
coordinateLists = []
value = {
"MapData":(
(1,0,0,1),
(0,1,1,0)
),
"TestPoint":(
(16, 15),
(18, 4),
(13, 2),
(5, 2),
(4, 12),
(14, 2)
)
}

# 行数
rowLength = len(value["MapData"])
# 列数
colLength = len(value["MapData"][0])


def getAndExtend(origin, x, y):
  if x>0 and x<rowLength and y>0 and y<colLength:
    area = getRoundCoordinate(x, y)
    if len(area)>0:
      origin.extend(area)
  return origin


def getRoundCoordinate(x,y):
  #print("###%d, %d" % (x, y))
  coordinateList = []
  if (x,y) not in coordinateHasTraversed:
    coordinateHasTraversed.append((x,y))
    if value["MapData"][x][y] == 0:
      coordinateList.append((x, y))
    else:
      return coordinateList
    
    coordinateList = getAndExtend(coordinateList, x-1, y)
    coordinateList = getAndExtend(coordinateList, x+1, y)
    coordinateList = getAndExtend(coordinateList, x, y-1)
    coordinateList = getAndExtend(coordinateList, x, y+1)
    if x-1 > 0:
      up = getRoundCoordinate(x-1, y)
      if len(up)>0:
        coordinateList.extend(up)
    if x+1 < rowLength:
      down = getRoundCoordinate(x+1, y)
      if len(down)>0:
        coordinateList.extend(down)
    if y-1 > 0:
      left = getRoundCoordinate(x, y-1)
      if len(left)>0:
        coordinateList.extend(left)
    if y+1 < colLength:
      right = getRoundCoordinate(x, y+1)
      if len(right)>0:
        coordinateList.extend(right)
  return coordinateList

def main():
  for indexX in range(rowLength):
    for indexY in range(colLength):
      # 没遍历过
      #print("***%d, %d" % (indexX, indexY))
      coordinateArea = getRoundCoordinate(indexX, indexY)
      if len(coordinateArea) > 0:
        #print(coordinateArea)
        coordinateLists.append(coordinateArea)
  print(coordinateLists)


if __name__ == '__main__':
  main()
  # print(__name__)
