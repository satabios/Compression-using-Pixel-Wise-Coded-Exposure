import numpy as np

def genBump(bumpSize, RowSize, ColSize, FrameNum):
    BumpTime = np.zeros((RowSize, ColSize), dtype=np.int)
    Mask = np.random.rand(RowSize, ColSize)
    for i in range(FrameNum-bumpSize+1):
        BumpTime[np.logical_and((i / (FrameNum-bumpSize+1)) < Mask, Mask <= ((i+1) / (FrameNum-bumpSize+1)))] = i
    sens_cube = np.zeros((FrameNum, RowSize, ColSize))

    for row in range(RowSize):
        for col in range(ColSize):
            start = BumpTime[row, col]
            sens_cube[start:start + bumpSize, row, col] = 1

    return sens_cube

# sens_cube_mat = genBump(3,5,5,13)
