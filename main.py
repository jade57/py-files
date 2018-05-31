
#Event Generator

import dice_machine

class Table:
    name = None
    events = []

class Event:
    name = None

class Range:
    def __init__(self, name, minVal, maxVal):
        self.name = name
        self.minVal = minVal
        self.maxVal = maxVal
    def SetRange(self, minIn, maxIn):
        self.minVal = minIn
        self.maxVal = maxIn

class Sector:
    name = None
    eventRange = []

class Controller:
    day = 0
    
    def NextDay(self):
        self.day += 1
        dayRoll = dice_machine.RollD(20)
        for span in SectorCurrent.eventRange:
            if dayRoll >= span.minVal and dayRoll <= span.maxVal:
                return print(str(dayRoll)+": An event was triggered on the "+str(span.name)+" table!")
class MECS:
    name = None
    subsystems = ["P","E","C"]

    def __init__(self, name):
        self.name = name

class Crew:
    name = None
    hp = 10
    room = None

    def __init__(self, name, room):
        self.name = name
        self.room = room
    
    def ChangeRoom(self):

        while True:
            
            print("Where should "+self.name+" be moved?\n")
            for i in range(0, len(ROOMS)):
                print("("+str(i+1)+") "+ROOMS[i].name)
            where = input("\nChoice: ")
            print("")
            where = int(where)-1
            
            if where in range(0, len(ROOMS)):
                oldRoom = self.room.name
                self.room = ROOMS[where]
                print(self.name+" has been moved from "+oldRoom+" to "+self.room.name)
                return

            print("Room not found. Try again...")

def CrewStatus():
    for i in range(0, len(CrewMembers)):
        print(CrewMembers[i].name+"\n-- Room: "+CrewMembers[i].room.name+"\n-- Health: "+str(CrewMembers[i].hp)+"\n")

def MoveCrew():
    while True:
            
        print("Who would you like to move?\n")
        for i in range(0, len(CrewMembers)):
            print("("+str(i+1)+") "+CrewMembers[i].name+" - "+CrewMembers[i].room.name)
        
        who = input("\nChoice: ")
        print("")
        who = int(who)-1
        
        if who in range(0, len(CrewMembers)):
            CrewMembers[who].ChangeRoom()
            return
        
        print("Not a valid selection! Try again...")

#define global vars
EVENT_TYPES = ["EVENTS","MEETINGS","OTHER"]
GC = Controller()

#init Sectors
Sector1 = Sector()
Sector1.name = "Alpha Sector"
Sector1.eventRange = [Range("Nothing",1,9),Range("Events",10,13),Range("Meetings",14,15),Range("Other",16,20)]

#init Ship
MECS_LABELS = ["Medbay","Engines","Comms","Systems"]
ROOMS = ["","","",""]
CrewMembers = ["","","",""]

for i in range(0, len(MECS_LABELS)):
    ROOMS[i] = MECS(MECS_LABELS[i])

for i in range(0, len(ROOMS)):
    CrewMembers[i] = Crew("Jenkins "+str(i+1),ROOMS[i])

SectorCurrent = Sector1

action = ""

while action != "exit":
    
    print("-------------\nDay: "+str(GC.day)+"\n-------------")
    print("What would you like to do?\n")
    action = input("(1) Continue\n(2) Crew Status\n(3) Move Crew Member\n\nChoice: ")
    print("")

    #test = 3 #int 3
    #test == 3 #bool with value of True
    #test == 7 #bool with value False

    if action == "1":
        GC.NextDay()
    elif action == "2":
        CrewStatus()
    elif action == "3":
        MoveCrew()
    

'''print(SectorCurrent.name)
for i in SectorCurrent.eventRange:
    print(i.name)
    print(i.minVal)
    print(i.maxVal)
'''
    