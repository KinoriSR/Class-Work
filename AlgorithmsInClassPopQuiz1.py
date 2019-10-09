#Find maximum sequence sum in input sequence.
#find the sum of the sequences within L
def sumSeq(L):
  total=0
  L_total=[]
  #make all possible sequences that start at beginning of this list
  for i in range(len(L)):
    total+=L[i]
    L_total.append((total))
  #returns a list of tuples that have total so far and end index
  return L_total

#find the maximum sequence
def findSeq(L):
  #list to save all possiblities
  possible=[]
  #send all possible sequence starting points to sumSeq()
  for i in range(len(L)):
    possible.append(sumSeq(L[i:]))
  #tuple to track max, start, end
  maximum=[0,0,0]
  for y in range(len(possible)):
    for x in range(len(possible[y])):
      #update max
      if possible[y][x]>maximum[0]:
        maximum=[possible[y][x],y+1,y+x+1]
  return maximum

#test cases
Input1=[-2, 1,-3, 4,-1, 2, 1, -5, 4]
Input2=[2, 0, 3, -2]
Input3=[8,-19, 5, -4, 20]
Input4=[2, 18, -22, 20, 8, -6, 10, -24, 13, 3]

#Outputs for the test cases
triple1=findSeq(Input1)
print ("The maximum sequence in Input1 is from index", triple1[1], "to", triple1[2], "with a sum of", triple1[0], ".")
triple2=findSeq(Input2)
print ("The maximum sequence in Input2 is from index", triple2[1], "to", triple2[2], "with a sum of", triple2[0], ".")
triple3=findSeq(Input3)
print ("The maximum sequence in Input3 is from index", triple3[1], "to", triple3[2], "with a sum of", triple3[0], ".")
triple4=findSeq(Input4)
print ("The maximum sequence in Input4 is from index", triple4[1], "to", triple4[2], "with a sum of", triple4[0], ".")
