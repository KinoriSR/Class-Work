#Check if a graph is connected or not connected, directed or not directed and complete or not compelete
def check(M):
  #0 if not connected 1 if connected
  connect=1
  #0 if undirected 1 if directed
  direct=0
  #0 if not complete 1 if complete
  complete=0
  length=len(M)
  #total of all edges to track if complete
  total=0
  for i in range(length):
    #sum of edges in a row to track if connected
    Sum=0
    for j in range(length):
      #check if directed - this has a problem if there are 2 directed edges of equal weights, but that case is equivalent to not directed
      item=M[i][j]
      if item!=M[j][i]:
        direct=1
      #if last item in list check if connected - check sum!=0 if so then disconnected
      Sum+=item
      if j==length-1: 
        if Sum==0:
          connect=0
      #check if complete if sum of every row is length-1
        total+=Sum
  if total == length**2-length:
    complete=1

  if connect==1:
    print('connected')
  else:
    print('not connected')
  if complete==1:
    print('complete')
  else:
    print('not complete')
  if direct==1:
    print('directed')
  else:
    print('undirected')
  #return in case another method wants to use this info not necessary here though
  return [direct,connect,complete]

#Inputs impletemented as adjacency matrices of the format if vertices A,B,C,D
#  A  B  C  D 
#A
#B
#C
#D
#        A,B,C,D,E,F
Input1=[[0,1,1,0,0,0],[1,0,1,0,0,0],[1,1,0,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,1,0,0,0]]
#        A,B,C,D,E
Input2=[[0,1,1,0,0],[1,0,0,1,0],[1,0,0,1,0],[0,1,1,0,0],[0,0,0,0,0]]
#       A,B,C,D
Input3=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
#        A,B,C,D,E
Input4=[[0,1,0,1,0],[1,0,1,0,0],[0,0,0,1,0],[1,0,1,0,1],[1,0,0,0,0]]

print('')
print('The graph, Input1, has the properties:')
Result1=check(Input1)
print('')
print('The graph, Input2, has the properties:')
Result2=check(Input2)
print('')
print('The graph, Input3, has the properties:')
Result3=check(Input3)
print('')
print('The graph, Input4, has the properties:')
Result4=check(Input4)
