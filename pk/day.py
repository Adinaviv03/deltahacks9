##from task import task

class task:

    name = ""
    length = 1 # 30 mins
    time = 0
    isBreak = True
    isMandatory = False

    def __init__(self) -> None:
        pass

    def __init__(self, name, length):
        self.name = name
        self.length = length*2 ##converts to half hour blocks
        self.isBreak = False




class day:
    
    start = 0
    end = 23
    numBlocks = 48 ##unit of half hours
    inputtedTaskList = []
    schedule = []

    def __init__(self, startTime, endTime):
        self.start = startTime
        self.end = endTime
        self.numBlocks = (self.end - self.start)*2
        for i in range(self.numBlocks):
            self.schedule.append(task())

    @staticmethod
    def displayTime(time):
        if time <= 12:
            output = str(time) + "am"
            return output
        
        pmTimes = {
            13: "1",
            14: "2",
            15: "3",
            16: "4",
            17: "5",
            18: "6",
            19: "7",
            20: "8",
            21: "9",
            22: "10",
            23: "11"
        }
        output = str(pmTimes[time]) + "pm"
        return output

    def addTask(self, newTask):
        self.taskList.append(newTask)
        
    def createSchedule(self):
        hoursOfWork = 0
        for task in self.taskList:
            hoursOfWork += task.length
        
        if hoursOfWork > self.numBlocks:
            print("Not enough time to finish tasks, edit time or number of tasks")
            return
        
        totalBreakTime = (self.numBlocks - hoursOfWork)
        singleBreakTime = totalBreakTime/(len(self.taskList) - 1)

        break1 = task()
        break1.length = singleBreakTime
        
        newTaskList = []
        for task in self.inputtedTaskList:
            newTaskList.append(task)
            newTaskList.append(break1)
        newTaskList = newTaskList[:-1]


        currentIndex = 0
        for task in self.inputtedTaskList:
            blocks = task.length
            for i in range(currentIndex, currentIndex + blocks):
                self.schedule[i] = task
            currentIndex += blocks

    def displaySchedule(self):
        blockTime = self.start
        last = ""
        for block in self.schedule:
            if (last == block.name):
                print("|")
            else:
                print(day.displayTime(blockTime))
                print(block.name)
            blockTime += 1
            last = block.name




        

        
