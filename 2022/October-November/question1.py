# 1a
jobs = [[None, None] for i in range(100)]
numberOfJobs = 0

# 1b
def Initialise():
    for item in jobs:
        item[0] = -1
        item[1] = -1
    numberOfJobs = 0

# 1c
def AddJob(job, priority):
    i = 0
    flag = False

    while i < len(jobs):
        if jobs[i][0] == -1:
            flag = True
            break

        i += 1
    
    if flag: 
        jobs[i][0], jobs[i][1] = job, priority
        print("Added!")
        InsertionSort()
    else: print("Not added!")

# 1e
def InsertionSort():
    master = slave = -1

    for master in range(1, len(jobs)):
        key = jobs[master]
        if key[1] == -1: break
        slave = master - 1
        while slave >= 0 and key[1] < jobs[slave][1]:
            jobs[slave + 1] = jobs[slave]
            slave -= 1
        jobs[slave + 1] = key

# 1f
def PrintArray():
    for item in jobs:
        if item[0] != -1:
            print(f"{item[0]} priority {item[1]}")
        else: break

# 1d
# Main Program
Initialise()
while True:
    PrintArray()
    job = input("Enter job number: (N to exit)\n>>> ")
    if job != "N":
        job = int(job)
        priority = int(input("Enter priority:\n>>> "))
        AddJob(job, priority)
    else: break

PrintArray()