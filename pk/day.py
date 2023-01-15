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
            self.schedule.append(task("none", 1))
        

    @staticmethod
    def displayTime(time):
        pmTimes = {
            12: "12",
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
        
        stringTime = str(time)

        if time < 12:
            if stringTime[-2:] == ".5":
                output = stringTime[:-2]
                output += ":30am"
                return output
            output = str(int(time)) + "am"
            return output


        elif time == 0 or time == 24:
            if stringTime[-2:] == ".5":
                output = "12:30am"
                return output
            output = "12am"
            return output
        
        
        elif stringTime[-2:] == ".5":
            output = stringTime[:-2]
            output = str(pmTimes[int(output)])
            output += ":30pm"
            return output
        output = str(pmTimes[time]) + "pm"
        return output

    def addTask(self, newTask):
        self.inputtedTaskList.append(newTask)
        
    def createSchedule(self):
        
        hoursOfWork = 0
        for myTask in self.inputtedTaskList:
            hoursOfWork += myTask.length
        
        if hoursOfWork > self.numBlocks:
            print("Not enough time to finish tasks, edit time or number of tasks")
            return
        
        totalBreakTime = (self.numBlocks - hoursOfWork)
        singleBreakTime = int(totalBreakTime/(len(self.inputtedTaskList) - 1))

        break1 = task("break", singleBreakTime/2)
        
        newTaskList = []
        for myTask in self.inputtedTaskList:
            newTaskList.append(myTask)
            newTaskList.append(break1)
        newTaskList = newTaskList[:-1]

    
        currentIndex = 0
        for myTask in newTaskList:
            blocks = int(myTask.length)
            print(blocks)
            for i in range(currentIndex, currentIndex + blocks):
                self.schedule[i] = myTask
            currentIndex += blocks

    def displaySchedule(self):
        
        blockTime = self.start
        realTime = self.start
        last = ""
        for block in self.schedule:
            if (last == block.name):
                print("|")
            else:
                print(day.displayTime(realTime), "-", block.name)
                print("|")
            blockTime += 1
            realTime += 0.5
            last = block.name
        




        

        
