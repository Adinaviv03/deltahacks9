from pk.day import day
from pk.day import task





class mainn:
    print("hello world")
    day1 = day(12, 19)
    print("My day starts at", day1.displayTime(day1.start) , "and ends at", day1.displayTime(day1.end))
    print("I have", day1.numBlocks, "blocks available today!")
    task1 = task("walk dogs", 1)
    task2 = task("clean house", 3)
    task3 = task("get groceries", 2)
    day1.addTask(task1)
    day1.addTask(task2)
    day1.addTask(task3)
    day1.createSchedule()
    day1.displaySchedule()
    
