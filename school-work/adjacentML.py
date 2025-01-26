#Graph = ((['a','b','c','d']), (('a' ,'d'), ('a', 'b'), ('a','c'), ('b', 'c'), ('d', 'a'), ('d', 'c')))
#Vertices = [a,b,c,d]
#Edges = (a ,d), (a, b), (a,c), (b, c), (d, a), (d, c)

adjacencyMatrix = [
    [0,1,1,1],#a
    [0,0,1,0],#b
    [0,0,0,0],#c
    [1,1,1,0]#d
]


ajacencyList = [
      ['b', 'c' ,'d'],
      ['c'],
      [],
      ['a','b','c']
]

dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

def matrixEdges(adjacencyMatrix):
    for i in range(0,4):
        for e in range(0,4):
            if adjacencyMatrix[i][e] == 1:
                    print(f"{dictionary[i]} -> {dictionary[e]};", end="  ")
        if adjacencyMatrix[i] == [0,0,0,0]:
                print(f"{dictionary[i]} -> has no edges", end = " ")
        print()


def listEdges(ajacencyList):
    for i in range(0,4):
        if ajacencyList[i] == []:
                  print(f"{dictionary[i]} -> has no edges", end = " ")
        for e in range(0, len(ajacencyList[i])):
             print(f"{dictionary[i]} -> {ajacencyList[i][e]}: ", end=" ")
        print()
                     

def main():
      print("Adjacency Matrix: ")
      matrixEdges(adjacencyMatrix)
      print()
      print("Adjacency List:  ")
      listEdges(ajacencyList)

if __name__ == '__main__':
    main()
