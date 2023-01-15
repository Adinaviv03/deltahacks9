task = []
time = []

const mainDiv = document.querySelector('#mainDiv')
const listSection = document.querySelector('#planSection')


button.onclick = function() {
  var output = document.createElement('li');
  output.innerHTML = document.getElementById('task').value + '   --    ' + document.getElementById('time').value + ' minutes';
  task.push(document.getElementById('task').value)
  time.push(document.getElementById('time').value)
  listSection.appendChild(output);
};

mainDiv.appendChild(button);


function planDay() {
    const beginT = timeSet()[0]
    const finishT = timeSet()[1]
    console.log(beginT)

}

function timeSet() {
    const startT = document.querySelector('#startTime').value
    const endT =  document.querySelector('#endTime').value

    x = [startT, endT]

    return x

}

function convertToBinarySchedule(myDay) {
    let newList = [];
    for (let day of myDay.schedule) {
        let bit = 0;
        if (day.name == "break") {
            bit = 1;
        }
        newList.push(bit);
    }
    return newList
}

class Task {
    constructor(name = "", length = 1) {
        this.name = name;
        this.length = length * 2;
        this.isBreak = false;
    }
}


class Day {

    constructor(startTime, endTime) {
        this.start = startTime;
        this.end = endTime;
        this.numBlocks = (this.end - this.start) * 2;
        this.inputtedTaskList = [];
        this.schedule = [];

        for (let i = 0; i < this.numBlocks; i++) {
            this.schedule.push(new Task("none", 1));
        }
    }

    static displayTime(time) {
        let pmTimes = {
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
            23: "11",
        };

        let stringTime = time.toString();
        
        if (time < 12) {
            if (stringTime.endsWith(".5")){
                let output = stringTime.slice(0, -2);
                output += ":30pm";
                return output;
            }
            let output = time + "am";
            return output;
        } else if (time === 0 || time === 24) {
            if (stringTime.endsWith(".5")){
                output += "12:30am";
                return output;
            }
            return "12am";
        }

        else if (stringTime.endsWith(".5")) {
            let output = stringTime.slice(0, -2);
            output = pmTimes[parseInt(output)];
            output += ":30pm";
            return output;
        }
        let output = pmTimes[time] + "pm";
        return output;
    }

    addTask(newTask) {
        this.inputtedTaskList.push(newTask);
    }

    createSchedule() {
        let hoursOfWork = 0;
        for (let myTask of this.inputtedTaskList) {
            hoursOfWork += myTask.length;
        }

        if (hoursOfWork > this.numBlocks) {
            console.log("Not enough time to finish tasks, edit time or number of tasks");
            return;
        }

        let totalBreakTime = this.numBlocks - hoursOfWork;
        let singleBreakTime = Math.floor(totalBreakTime / (this.inputtedTaskList.length - 1));

        let break1 = new Task("break", singleBreakTime / 2);

        let newTaskList = [];
        for (let myTask of this.inputtedTaskList) {
            newTaskList.push(myTask);
            newTaskList.push(break1);
        }
        newTaskList.pop();

        let currentIndex = 0;
        for (let myTask of newTaskList) {
            let blocks = Math.floor(myTask.length);
            console.log(blocks);
            for (let i = currentIndex; i < currentIndex + blocks; i++) {
                this.schedule[i] = myTask;
            }
            currentIndex += blocks;
        }
    }

    displaySchedule() {
        let blockTime = this.start;
        let realTime = this.start;
        let last = "";
        for (let block of this.schedule) {
            if (last === block.name) {
                console.log("|");
            } else {
                console.log(Day.displayTime(realTime), "-", block.name);
                console.log("|");
            }
        blockTime = blockTime +1
        realTime += 0.5
        last = block.name
        }
    }

}

console.log("hello world");
let day1 = new Day(8, 19);
console.log("My day starts at", Day.displayTime(day1.start) , "and ends at", Day.displayTime(day1.end));
console.log("I have", day1.numBlocks, "blocks available today!");
let task1 = new Task("walk dogs", 1);
let task2 = new Task("clean house", 3);
let task3 = new Task("get groceries", 2);
day1.addTask(task1);
day1.addTask(task2);
day1.addTask(task3);
day1.createSchedule();
day1.displaySchedule();




