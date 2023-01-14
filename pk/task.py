class task:

    name = ""
    length = 1
    isBreak = True

    def __init__(self) -> None:
        pass

    def __init__(self, name, length):
        self.name = name
        self.length = length*2 ##converts to half hour blocks
        self.isBreak = False

