#mergesort with 3 lists

#merge 3 lists
def merge(L1,L2,L3):
  retL=[]
  i=0
  j=0
  k=0
  while i<len(L1) and j<len(L2) and k<len(L3):
      if L1[i]<=L2[j] and L1[i]<L3[k]:
          retL.append(L1[i])
          i+=1
      elif L2[j]<=L1[i] and L2[j]<L3[k]:
        retL.append(L2[j])
        j+=1
      elif L3[k]<=L1[i] and L3[k]<=L2[j]:
        retL.append(L3[k])
        k+=1
  if i==len(L1):
    L2=L2[j:]
    L3=L3[k:]
    retL=merge2(L2,L3,retL)
  elif j==len(L2):
    L1=L1[i:]
    L3=L3[k:]
    retL=merge2(L1,L3,retL)
  else:
    L1=L1[i:]
    L2=L2[j:]
    retL=merge2(L1,L2,retL)
  return retL

#merge 2 lists
def merge2(L1,L2,retL):
  i=0
  j=0
  while i<len(L1) and j<len(L2):
    if L1[i]<L2[j]:
      retL.append(L1[i])
      i+=1
    else: 
      retL.append(L2[j])
      j+=1
  if i<len(L1):
    for a in range(i,len(L1)):
      retL.append(L1[a])
  else:
    for a in range(j,len(L2)):
      retL.append(L2[a])
  return retL

#mergesort
def mergesort(L):
  #base case
  if len(L)==2:
    return merge2(L[:1],L[1:],[])
  if len(L)==1:
    return L
  #divide list
  third=len(L)//3
  twothird=2*(len(L)//3)
  L1=mergesort(L[:third])
  L2=mergesort(L[third:twothird])
  L3=mergesort(L[twothird:])
  #merge them
  return merge(L1,L2,L3)

Input1=[35, 28, 23, 15, 12, 10, 6]	
Input2=[12, 12, 23, 4, 6, 6, 10, -35, 28, 12]
print (mergesort(Input1))
print (mergesort(Input2))
