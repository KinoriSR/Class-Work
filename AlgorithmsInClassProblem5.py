#Implement Prim's algorithm to find the minimum spanning tree or deem the graph not connected.
#I ran out of time on this one because of a silly bug. Found the bug after class with not too much effort... doh!
#  \/
# ('')
#>( )<
#>( )<
#>( )<

from math import inf
def prim(G):
    rowlength=len(G[0])
    #storing tuple of (i,j,value)
    edges=[]
    #list of vertices
    vert=[0]
    #for each vertex in list
    for i in range(rowlength):
        minedge=[0,0,inf]
        #visit each edge of each vertex
        for v in vert:
            for e in range(rowlength):
                if v!=e:
                    weight=G[v][e]
                    #if edge has less weight and leads to a not visited vertex
                    if minedge[2]>weight and (e not in vert):
                        minedge=[v,e,weight]
        if minedge[2]!=inf:
            #put minimum edge in list
            edges.append(minedge)
            #add new vertex
            vert.append(minedge[1])
        #not connected if all edges go to somewhere already visited and i hasn't reached the end yet
        elif i!=rowlength-1 and minedge[2]==inf:
            print("This tree is 'not connected'.")
            return None,None
    
    #formatting output
    S=0
    retedge=[]
    for i in range(len(edges)):
        S+=edges[i][2]
        retedge.append([edges[i][0]+1,edges[i][1]+1])
    print("This graph is connected.")
    return retedge, S
    
#connected
graph1 = [[0,32,inf,17,inf,inf,inf,inf,inf,inf],
          [32,0,inf,inf,45,inf,inf,inf,inf,inf],
          [inf,inf,0,18,inf,inf,5,inf,inf,inf],
          [17,inf,18,0,10,inf,inf,3,inf,inf],
          [inf,45,inf,10,0,28,inf,inf,25,inf],
          [inf,inf,inf,inf,28,0,inf,inf,inf,6],
          [inf,inf,5,inf,inf,inf,0,59,inf,inf],
          [inf,inf,inf,3,inf,inf,59,0,4,inf],
          [inf,inf,inf,inf,25,inf,inf,4,0,12],
          [inf,inf,inf,inf,inf,6,inf,inf,12,0]]
print('Running with input: graph1.')
edges, weight=prim(graph1)
if edges!=None:
    print('The minimum spanning tree has the edges:')
    print(edges)
    print('The tree weighs:',weight)
print()
#not connected
graph2 = [[0,32,inf,inf,inf,inf,inf,inf,inf,inf],
          [32,0,inf,inf,inf,inf,inf,inf,inf,inf],
          [inf,inf,0,18,inf,inf,5,inf,inf,inf],
          [inf,inf,18,0,10,inf,inf,3,inf,inf],
          [inf,inf,inf,10,0,28,inf,inf,25,inf],
          [inf,inf,inf,inf,28,0,inf,inf,inf,6],
          [inf,inf,5,inf,inf,inf,0,59,inf,inf],
          [inf,inf,inf,3,inf,inf,59,0,4,inf],
          [inf,inf,inf,inf,25,inf,inf,4,0,12],
          [inf,inf,inf,inf,inf,6,inf,inf,12,0]]
print('Running with input: graph2.')
edges, weight=prim(graph2)
if edges!=None:
    print('The minimum spanning tree has the edges:')
    print(edges)
    print('The tree weighs:',weight)
