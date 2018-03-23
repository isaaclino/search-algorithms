
import re
import sys
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")

vertices=[]
edges=[]
#--------------------------------------------------------------------------------
def BellmanFord(G):
    pathPairs=[]
    edges = []
    
    # Fill in your Bellman-Ford algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    
    counter = 0
    
    for i in G[1]:
        vertexPath = i[:]
        for vertex in range(len(vertexPath)):
            edgePath = []
            if vertexPath[vertex] != float("inf"):
                    edgePath.append([counter,vertex])
                    edgePath.append(vertexPath[vertex])
                    edges.append(edgePath)
            if vertex == counter:
                vertexPath[vertex] = 0
            else:
                    vertexPath[vertex] = float("inf")

        counter += 1
        pathPairs.append(vertexPath);


    for i in range(len(pathPairs)):
        for j in range(len(G[0])-1):
            for k in range(len(edges)):
                if pathPairs[i][edges[k][0][0]] + int(edges[k][1]) < pathPairs[i][edges[k][0][1]]:
                    pathPairs[i][edges[k][0][1]] = pathPairs[i][edges[k][0][0]] + int(edges[k][1])

    return pathPairs


#--------------------------------------------------------------------------------
def FloydWarshall(G):
    pathPairs=[]
    
    
    pathPairs= helper_SwapEdges(G[1])
    for i in range(0, len(G[0])):
        pathPairs[i][i] = 0
    
    for k in range(0, len(G[0])):
        for i in range(0, len(pathPairs)):
            for j in range(0, len(pathPairs[i])):
                result = pathPairs[i][k] + pathPairs[k][j]
                
                if result < pathPairs[i][j]:
                    pathPairs[i][j] = result
    return pathPairs


def helper_SwapEdges (edge):
    for i in range(0 , len(edge)):
        for j in range(0 , len(edge[i])):
            if type(edge[i][j]) is str:
                edge[i][j] = int(edge[i][j])
    return edge


#--------------------------------------------------------------------------------
def readFile(filename):
    global vertices
    global edges


    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)

            if int(source) >= len(vertices) or int(sink) >= len(vertices):
                print("Attempting to insert an edge between "+str(source)+" and "+str(sink)+" in a graph with "+str(len(vertices))+" vertices")
                quit(1)

            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
  
    # TODO: Debugging
    #for i in G:
    #print(i)
    return (vertices,edges)


#--------------------------------------------------------------------------------
def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)

    pathLengths=[]
  
    if algorithm == 'b' or algorithm == 'B':
        pathLengths=BellmanFord(G)
        print "Path Lenghts: ", pathLengths
  
    if algorithm == 'f' or algorithm == 'F':
        pathLengths=FloydWarshall(G)
        print "Path Lenghts: ", pathLengths

    if algorithm == "both":
      
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
    
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
    
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment2.py -<f|b> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print('python assignment2.py -<f|b> <input_file>')
        quit(1)
    main(sys.argv[2],sys.argv[1])

# Assignment 2 -  CS141 - Isaac Lino

