
#Event Generator

import dicemachine
from easygui.easygui import *

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
    sector = 0

    def NextDay(self):
        self.day += 1
        dayRoll = dicemachine.RollD(20)
        for span in self.sector.eventRange:
            if dayRoll >= span.minVal and dayRoll <= span.maxVal:
               return msgbox("An event was triggered on the "+str(span.name)+" table!")

class Subsystem:
    name = None
    damage = 0
    sid = None

    def __init__(self, name):
        self.name = name
        self.sid = name[:1]
    
    def GetSeverity(self):
        if self.damage == 0:
            return "No Damage"
        else:
            return "Severity Level "+str(self.damage)
        
class MECS:
    name = None
    subsystems = [Subsystem("Physical"),Subsystem("Electrical"),Subsystem("Computerized")]

    def __init__(self, name):
        self.name = name



class Crew:
    name = None
    hp = 10
    room = None

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def GetHealth(self):
        if self.hp >= 10:
            return "Perfect"
        elif self.hp >= 8:
            return "Great"
        elif self.hp >= 6:
            return "Fair"
        elif self.hp >= 4:
            return "Poor"
        elif self.hp >= 1:
            return "Terrible"
        else:
            return "Dead"
    
    def ChangeRoom(self):
        while True:
            where = buttonbox("Where should "+self.name+" be moved?\n","Room Reassignment",MECS_LABELS)
            for room in ROOMS:
                if where == room.name:
                    oldRoom = self.room.name
                    self.room = room
                    msgbox(self.name+" has been moved from "+oldRoom+" to "+self.room.name)
                    return
            print("Room not found. Try again...")

def ShipStatus():
    textStr = ""
    for room in ROOMS:
        textStr += ("-----\n"+room.name+"\n-----\n")
        for sub in room.subsystems:
            textStr += (sub.name+" Components:\n"+"    Damage: "+sub.GetSeverity()+"\n")
        textStr += "\n"
    textStr += ("\n-----\nCrew Status\n-----\n")
    for crew in CrewMembers:
        textStr += ("\n"+crew.name+"\n-- Room: "+crew.room.name+"\n-- Health: "+crew.GetHealth()+"\n")
    
    textbox(textStr)
        
def MoveCrew():
    while True:
        crewNames = []
        for crew in CrewMembers:
            crewNames.append(crew.name)
        who = buttonbox("Who would you like to move?","Pick Crew",crewNames)
        
        for crew in CrewMembers:
            if who == crew.name:
                crew.ChangeRoom()
                return
        
        print("Not a valid selection! Try again...")

#init Sectors
Sector1 = Sector()
Sector1.name = "Alpha Sector"
Sector1.eventRange = [Range("Nothing",1,9),Range("Events",10,13),Range("Meetings",14,15),Range("Other",16,20)]

#init Ship
MECS_LABELS = ["Medbay","Engines","Comms","Systems"]
ROOMS = [None]*4
CrewMembers = [None]*4

#define global vars
EVENT_TYPES = ["EVENTS","MEETINGS","OTHER"]
GC = Controller()
GC.sector = Sector1

for i in range(0, len(MECS_LABELS)):
    ROOMS[i] = MECS(MECS_LABELS[i])

for i in range(0, len(ROOMS)):
    CrewMembers[i] = Crew("Jenkins "+str(i+1),ROOMS[i])

OPTIONS=["Continue","Crew Status","Move Crew Member"]

def main():

    action = ""

    while action != "exit":
        
        action = buttonbox("What would you like to do?","Day: "+str(GC.day),OPTIONS)

        if action == OPTIONS[0]:
            GC.NextDay()
        elif action == OPTIONS[1]:
            ShipStatus()
        elif action == OPTIONS[2]:
            MoveCrew()

main()
