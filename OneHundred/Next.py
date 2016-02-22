input_str = input()

dim = [ int(x) for x in input_str.split(",")]

rowNum = dim[0]
colNum = dim[0]

collist = [[1 for col in range(colNum)] for row in range(rowNum)]

#print("row: %d " + rowNum)
#print("col: %d " + colNum)

for row in range(rowNum):
    for col in range(colNum):
        collist[row][col] = row * col

print(collist)

## multilist = []