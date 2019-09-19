#Split list with equal number of items and minimized "weight" (sum of items) difference

#Input: L list
#Output: Sum of items or "weight"
def findsum(L):
    Sum=0
    for i in range(len(L)):
        Sum+=L[i]
    return Sum

#Input: L list
#Output: Partition Lists L1 and L2 with minimized weight difference
def main(L):
    #create initial partition
    Hlength=len(L)//2
    L1=L[:Hlength]
    L2=L[Hlength:]
    #find partition weights
    sum1=findsum(L1)
    sum2=findsum(L2)
    
    #check items in L1 with L2 and see if weight can be reduced
    for i in range(Hlength):
        for j in range(Hlength):
            #see if the weights are the same, this would be a return condition because weights are equal (minimized difference)
            if sum1==sum2:
                return L1, sum1, L2, sum2
            #compare difference if items are switched
            olddiff=abs(sum2-sum1)
            newdiff=abs((sum2-L2[j]+L1[i])-(sum1-L1[i]+L2[j]))
            if newdiff<olddiff:
                #alter weights with switch
                sum1=sum1-L1[i]+L2[j]
                sum2=sum2-L2[j]+L1[i]
                #switch items
                hold=L1[i]
                L1[i]=L2[j]
                L2[j]=hold
    
    return L1, sum1, L2, sum2

Input0=[10,20,11,9]
Input1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Input2=[10, 20, 15, 5, 25, 100]
Input3=[10,2,5,6,7,40,8,3,1,4,1,5,9,2]
print main(Input0)
print main(Input1)
print main(Input2)
print main(Input3)
