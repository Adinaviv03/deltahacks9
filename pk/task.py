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

    def __init__(self, name, length, time):
        self.name = name
        self.length = length*2 ##converts to half hour blocks
        self.time = time
        self.isBreak = False
        self.isMandatory = True

