#Trinary search - instead of binary search with 2 cutting the list in half, this cuts the list into thirds
def trisearch(L,n):
  #prepare to divide the list
  length=len(L)
  third = length//3
  twothird = 2*(length//3)

  #search if less than 3
  if length==1 and L[0]==n:
    return 0
  elif length==1 and L[0]!=n:
    return 'Does not contain.'
  elif length==2:
    if L[0]==n:
      return 0
    elif L[1]==n:
      return 1
    else:
      return 'Does not contain.'

  #divide the list
  L1=L[:third]
  L2=L[third:twothird]
  L3=L[twothird:]
 # print (L1)
 # print (L2)
 # print (L3)
  if n<L[third]:
    #recur with first third
    subposition=trisearch(L1,n)
    if subposition=='Does not contain.':
      return 'Does not contain.'
    else:
      return subposition
  elif L[third]<=n and n<L[twothird]:
    #recur with second third
    subposition=trisearch(L2,n)
    if subposition=='Does not contain.':
      return 'Does not contain.'
    else:
      return subposition+third
  else:
    #recur with last third
    subposition=trisearch(L3,n)
    if subposition=='Does not contain.':
      return 'Does not contain.'
    else:
      return subposition+twothird

Find1=8
Input1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
position1 =trisearch(Input1,Find1)
print ('The item you are looking for in Input1 is in position:',position1)
Find2=32 
Input2= [1, 5, 7, 9, 15, 30, 33, 37, 41, 42, 43, 65, 69]
position2=trisearch(Input2,Find2)
print ('The item you are looking for in Input2 is in position:',position2)
