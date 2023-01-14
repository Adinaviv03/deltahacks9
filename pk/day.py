from task import task

class day:
    
    start = 0
    end = 23
    numBlocks = 48
    taskList = []

    def __init__(self, startTime, endTime):
        self.start = startTime
        self.end = endTime
        self.numBlocks = (self.end - self.start)*2
    
    def displayTime(self, time):
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
        
        if hoursOfWork > self.numBlocks/2:
            print("Not enough time to finish tasks, edit time or number of tasks")
            return

        
