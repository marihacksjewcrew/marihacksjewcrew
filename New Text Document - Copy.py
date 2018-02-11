dataList=[20,30,40,25,35,45,26,27,39,84,55,28,95,92,34,67,45,74,74,65,99,89,112,90,89,83,74,40,20,20,29,28,20,23,24,2,52,62,27,23,24,24,23,25,23,24,25,24,24,23,25,26,23,30,34,36,37,39,38,37,38,39,42,45,41,46,47,48,49,49,51,52,49,58,59,59,63,64,67,64,68,63,69,68,64,63,62,65,68,69,75,76,74,78,79,76,79,80,82,83,84,85,83,84,86,87,88,89,92,93,94,95,90,87,85,83,76,72,67,62,57,51,48,40,34,20]
LTavgList=[]
STMavgList=[]
LTMavgList=[]

def long_term():

    #long term average
    LTavgList.append(dataList[0])
    for i in range(len(dataList)-1):
        LTavgList.append(round((((i+1)*LTavgList[i]+dataList[i+1])/(i+2)),2))

    #to view long term average values over a specific period of time
    print("Select the data range that you would like to analyze")
    LTBeg=int(input("Beginning: "))
    print("The number of data points in your list is", len(dataList))
    LTEnd=int(input("End: "))
    print(LTavgList[LTBeg-1:LTEnd])

def short_term_moving():

    #moving average
    STMavgListLen=int(input("Short term moving average time period: "))
    for i in range(len(dataList)-STMavgListLen+1):
        sum=0
        for j in range(i,STMavgListLen+i):
            sum+=dataList[j]
        STMavgList.append(round(sum/STMavgListLen,2))

def long_term_moving():

    #moving average
    LTMavgListLen=int(input("Long term moving average time period: "))
    for i in range(len(dataList)-LTMavgListLen+1):
        sum=0
        for j in range(i,LTMavgListLen+i):
            sum+=dataList[j]
        LTMavgList.append(round(sum/LTMavgListLen,2))
