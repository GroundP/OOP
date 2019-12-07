''' Algorithm
    문제설명 : n x m 크기의 바닥에 1x1x1 크기의 벽돌이 놓여 있습니다. 놓여 있는 벽돌 위로 비가 내리면 아래 그림과 물이 차오르게 됩니다.
    이때 우리는 최대로 모을 수 있는 빗물의 양을 구하려고 합니다. (1x1x1 공간에 모인 빗물의 양은 1입니다.)'''

def get_rain(buildings):
    max_val = max(buildings)

    rain_arr = []
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        leftMax = max(buildings[:i])
        center = buildings[i]
        rightMax = max(buildings[i + 1:])

        # center 기준으로 좌,우측 max층 중 작은 값에서 center를 뺀 값이 비에 잠긴 양
        if leftMax > center and rightMax > center:
            rain_arr.append((min(leftMax, rightMax) - center))
        else:
            rain_arr.append(0)

    return rain_arr

def solutaion(bricks):
    longitudinal = len(bricks[0])
    vertical = len(bricks)

    verArray = [] # 수직방향 Array
    for long in range(longitudinal):
        subarray = []
        for ver in range(vertical):
            subarray.append(bricks[ver][long])
        verArray.append(subarray)

    longRain = [] # 길이방향 차오르는 물
    for i in range(1, vertical - 1):
        longRain.append(get_rain(bricks[i]))

    verRain = [] # 수직방향 차오르는 물
    for i in range(1, longitudinal -1):
        verRain.append(get_rain(verArray[i]))

    longSum = 0 # 길이방향 빗물 양
    verSum = 0 # 수직 방향 빗물 양
    for i in longRain:
        for j in i:
            longSum += j

    for i in verRain:
        for j in i:
            verSum += j

    print(longRain)
    print(verRain)
    print(longSum)
    print(verSum)
    print("")

bricks1 = [[2,4,3,2,3,2], [3,1,1,4,1,3], [2,2,1,3,3,1] ]
bricks4 = [[5,5,5,5], [4,1,1,5], [3,1,1,5], [4,4,4,5]]
bricks2 = [[2,2,2], [1,2,2], [1,2,1]]
bricks5 = [[4,1,1,3,1], [4,1,2,0,2], [4,1,1,2,2]]
solutaion(bricks1)
solutaion(bricks4)
solutaion(bricks5)