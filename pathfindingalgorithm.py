import timeit
#Put the graph into a format the computer can use
def pathgraph() :
    return {       
        'A': {'B':22, 'C':9, 'D':12},
        'B': {'A':22, 'C':35, 'F':36, 'H':34},
        'C': {'A':9, 'B':35, 'D':4, 'E':65, 'F':42},
        'D': {'A':12, 'C':4, 'E':33, 'I':30},
        'E': {'C':65, 'D':33, 'F': 18, 'G': 23},
        'F': {'B':36, 'C':42, 'E': 18, 'G': 39, 'H':24},
        'G':{'E': 23, 'F':39, 'H':25, 'I':19},
        'H':{'B':34, 'F':24, 'G':25, 'I':19},
        'I':{'D':30, 'G':21, 'H':19} 
            }

#Bellman-Ford Algorithm
def bellmanford():
    start = 'A' #staring position
    nodedistance = {} #to hold the distance between each node
    shortestmoves = {} #shortest move from each node
    paths = pathgraph() #the graph itself

    #set nodes to infinity, and the paths that can be moved to none
    for i in paths:
        nodedistance[i] = float("inf")
        shortestmoves[i] = None
    #set the first node to 0
    nodedistance[start] = 0

    #update the distances
    for _ in range (len(paths) - 1):
        for j in paths:
            for moves in paths[j]:
                    #if distance is lower than current, correct it
                    if nodedistance[moves] > nodedistance[j] + paths[j][moves]:
                        nodedistance[moves], shortestmoves[moves] = nodedistance[j] + paths[j][moves], j

    #check for negative weight
    for i in paths:
        for moves in paths[i]:
            if nodedistance[moves] > nodedistance[i] +  paths[i][moves]:
                print('Negative weight found.')
                return None
            
    #create a list to put the information in
    i = 'I'
    print('The shortest route to ' + i + ' is:')
    bestpath = [i]
    i = shortestmoves[i]
    while i != None:
        bestpath.append(i)
        i = shortestmoves[i]

    while len(bestpath) != 0:
        print(bestpath.pop())

#Dijkstra's Algorithm
def dijkstra():
    start = 'A' #staring position
    nodedistance = {} #to hold the distance between each node
    shortestmoves = {} #shortest move from each node
    testpaths = [] #paths to check
    paths = pathgraph() #the graph itself

    #set nodes to infinity, and the paths that can be moved to none
    for i in paths:
        nodedistance[i] = float("inf")
        shortestmoves[i] = None
        testpaths.append(i)
    #set the first node to 0
    nodedistance[start] = 0
    #test all paths
    while len(testpaths) != 0:
        #set minroute to the shortest route
        minroute = testpaths[0]
        minvalue = nodedistance[minroute]
        for i in range(1, len(testpaths)):
            #if there is a shorter route, set minvalue to that route
            test = testpaths[i]
            if nodedistance[test] < minvalue:
                minroute = testpaths[i]
                minvalue = nodedistance[minroute]
        #when smallest route is found, remove from the test and save it
        smallnode = minroute
        testpaths.remove(smallnode)

        for i in paths[smallnode]:
            #check alternate routes, if smaller change course
            altroute = paths[smallnode][i] + nodedistance[smallnode]
            if nodedistance[i] > altroute:
                nodedistance[i] = altroute
                shortestmoves[i] = smallnode
    #create a list to put the information in
    i = 'I'
    print(shortestmoves)
    print('The shortest route to ' + i + ' is:')
    bestpath = [i]
    i = shortestmoves[i]
    while i != None:
        bestpath.append(i)
        i = shortestmoves[i]

    while len(bestpath) != 0:
        print(bestpath.pop())
            

#time results
bfResults = timeit.repeat(stmt=r"bellmanford()",setup="from pathfindingalgorithm import bellmanford",number=100)
print("Bellman-Ford Algorithm Results: "+str(bfResults)+ "average of "+ str(sum(bfResults)/len(bfResults)) + "milliseconds.")
dijkResults = timeit.repeat(stmt=r"dijkstra()",setup="from pathfindingalgorithm import dijkstra",number=100)
print("Dijkstra's Algorithm Results: " + str(dijkResults)+ "average of "+ str(sum(dijkResults)/len(dijkResults)) + "milliseconds.")

            
