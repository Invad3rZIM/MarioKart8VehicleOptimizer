from tablebuilder import buildTable, parseFile

class Engine:
    def __init__(self):
        self.matrix = [buildTable(parseFile("data/characters")),
                       buildTable(parseFile("data/karts")),
                       buildTable(parseFile("data/tires")),
                       buildTable(parseFile("data/gliders"))]

        self.categories = ["characters", "karts", "tires", "gliders"]
        self.metrics = ["Characters", "Speed", "Acceleration", "Weight", "Handling", "Traction", "Mini-Turbo", "Total"]
        self.writeMetrics()
        self.filters = []
        self.priorities = {}

    def writeMetrics(self):
        f = open("data/metrics", "a")

        for i in range(len(self.matrix)):
            f.write(self.categories[i] + "\n")

            for j in self.matrix[i]:
                string = ""
                for s in j:
                    string += str(s) + ","
                f.write(string[0:len(string)-1] + "\n")

    def processCommand(self, cmd):
        cmd = cmd.split(" ")
        if cmd[0] == "help":
            self.showHelp()
        if cmd[0] == "priority":
            self.setPriority(cmd[1:])

    def setPriority(self, args):
        if len(args) % 2 != 0:
            print("Priorities must follow the form [category] [rating] ...")

        index = 0

        while index < len(args):
            if args[index+1].isdigit():
                self.priorities[args[index]] = int(args[index+1])
            index += 2
    
    
    
    def showHelp(self):
        helpList = ["(h)elp\t displays a list of (helpful) commands",
                    "(p)riority\t allows you to set your priority list"]

        for item in helpList:
            print("\t",item)
        


    def welcome(self):
        print("Hi and welcome to Kirk's MK Optimizer!")
        print("This tool is designed to calculate optimal vehicles for Mario Kart 8")
        print("For a list of commands, enter 'help'. Enjoy!")


    def totals(self):
        combinations = 1

        for index in range(len(self.categories)):
            print(self.categories[index], len(self.matrix[index]))
            combinations *= len(self.matrix[index])

        print("for a total of", combinations, "combinations")

        

