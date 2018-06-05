import dicemachine

class Event:
    name = None
    value = 0
    table = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Table:
    name = None
    events = []
    size = 0
    
    def __init__(self, name):
        self.name = name

    def setSize(self, size):
        self.size = size
        
    def addEvent(self, event: Event):
        self.events[event.value] = event
        event.table = self


def PopulateTableEvents(eventType: str, rangeMin: int, rangeMax: int) -> list:
    events = []
    for i in range(rangeMin,rangeMax):
        events.append(eventType)
    return events

def test():
    DailyEventsTable = Table("Daily Events Table")
    SUBTABLES = ["NOTHING","EVENTS","MEETINGS","OTHER"]
    DAILY_EVENTS = []
    
    for subtable in SUBTABLES:
        roll = dicemachine.RollD(8)
        DAILY_EVENTS += [Table(subtable)]

    print(DAILY_EVENTS)
    
    #DailyEventsTable.setSize(len(DAILY_EVENTS))
    for i in range(0,len(DAILY_EVENTS)):
        DailyEventsTable.addEvent(Event(DAILY_EVENTS[i].name,i))

        print(DailyEventsTable.events)
        print(DailyEventsTable.events[i].table)

    print(DailyEventsTable.name+" :")
    print(DailyEventsTable.events)
    
    action = "y"
    while action != "q":
        #print(str(len(DAILY_EVENTS)))
        roll = dicemachine.RollD(len(DAILY_EVENTS))

        print(roll)
        print(DailyEventsTable.events[roll])
        
        action = input("Again? [ENTER] ('q' to quit)\n")
        
