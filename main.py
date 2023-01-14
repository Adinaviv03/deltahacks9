class main:
    print("hello world")


class day:
    
    start = 0
    end = 24
    numBlocks = 24

    def __init__(self, startTime, endTime):
        self.start = startTime
        self.end = endTime
        self.numBlocks = self.end - self.start