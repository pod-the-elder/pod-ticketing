import csv

with open('data\jobTickets.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    
    jobIDs = []
    calcPriorities = []
    tickDescs = []

    for row in csvReader:
        jobID = row[0]
        calcPriority = row[5]
        tickDesc = [6]

        jobIDs.append(jobID)
        calcPriorities.append(calcPriority)
        tickDescs.append(tickDesc)

    print(jobIDs)
    print(calcPriorities)
    print(tickDescs)

    #Pulls full detail of list

    scrapedID = input("Which job ID do you want to see more of? ")
    for row in csvDataFile:
        if int(scrapedID) == row[0]:
            print row
