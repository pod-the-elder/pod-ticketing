# Basic Priority Calculation Formula

def priorityCalc():
    priority = 0
    delayCons = raw_input("What is the Consiquence of Delay? ")
    failCons = raw_input("What is the Consiquence of Failure? ")
    priority = int(delayCons) + int(failCons)
    print(priority)

priorityCalc()

