def createMatrix():
    count = 0
    matrix = []
    while True: 
        try: 
            rows = int(input('Enter number of Rows: '))
            cols = int(input('Enter number of Cols: '))
        #if users enterd 2 for rows, ask for nums 2 tim
            if rows <= 0 or cols <= 0:
                print('Rows and Cols must be positive')
                continue
            break
        except ValueError:
            print('Rows and Cols must be NUMBERS')
    for i in range(0, rows):
        flag = True
        count += 1
        while flag:
            rowNumbers = input(f"Input numbers for Row {count}: ")
            listRowNumbers = rowNumbers.split(",")
            try:
                for i in range(0, len(listRowNumbers)):
                    value = int(listRowNumbers[i])
                if len(listRowNumbers) == cols:
                    flag = False
            except ValueError:
                print("You need to enter a Number")
                continue
            else:
                if len(listRowNumbers) != cols:
                    print("Enterd numbers don't equal column numbers.")
                    continue
        eachRow = []
        for i in range(0, len(listRowNumbers)):
            singleNums=int(listRowNumbers[i])
            eachRow.append(singleNums)
        matrix.append(eachRow)
    return matrix             



def multipleMatrix(matrixA, matrixB):
    if len(matrixA[0]) != len(matrixB):
        return None

    final = [] 
    for i in range(0, len(matrixA)):#i = rows
        rows = []
        for e in range(0, len(matrixB[0])):#e = cols
            result = 0
            for j in range(len(matrixB)):
                result += matrixA[i][j] * matrixB[j][e]
            rows.append(result)
        final.append(rows)
    return final

      
def main():
    flag = True
    while flag:
        print('Matrix A: ')
        matrixA = createMatrix()
        print('Matrix B: ')
        matrixB = createMatrix()

        matrix = multipleMatrix(matrixA, matrixB)
        if matrix == None:
            print('Matrix multiplication is invalid.')
            flag = True
        else:
            print(multipleMatrix(matrixA, matrixB))
            flag = False
main()