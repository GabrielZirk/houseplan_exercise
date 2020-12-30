import abc
from typing import List, Dict, Set, Tuple

class RoomOpening:
    def __init__(self, posx: float, posy: float, width: float, height: float):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

class Room:
    def __init__(self, type: str, area: float):
        valid_roomtypes = {"BEDROOM", "KITCHEN", "LIVINGROOM", "EATINKITCHEN", "STOREROOM", "TOILET", "BATHROOM", "CORRIDOR"}
        if type not in valid_roomtypes:
            raise ValueError(f"Invalid roomtype. Roomtype must be one of {valid_roomtypes}.")
        else:
            self.type = type
        self.area = area
        self.openings = dict()

    def __repr__(self):
        return f"{self.type}, {self.area}"

    def add_opening(self, orientation: str, ropening: RoomOpening):
        possible_orientation = {"SOUTH", "WEST", "NORTH", "EAST"}
        if orientation not in possible_orientation:
            raise ValueError(f"This is not a possible orientation. Orientation must be one of {possible_orientation}")
        else:
            if orientation not in self.openings.keys():
                self.openings[orientation] = [ropening]
            else:
                self.openings[orientation].append(ropening)

class Window(RoomOpening):
    def __init__(self, posx: float, posy: float, width: float, height: float, can_be_opened: bool):
        super().__init__(posx, posy, width, height)
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.can_be_opened = can_be_opened

    def __repr__(self):
        return f"Window"

class Door(RoomOpening):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2: Room):
        super().__init__(posx, posy, width, height)
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.room1 = room1
        self.room2 = room2
    def __repr__(self):
        return f"Door"

class HouseDoor(Door):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, security_door: bool, room2 = None):
        super().__init__(posx, posy, width, height, room1, room2)
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.room1 = room1
        self.room2 = room2
        self.security_door = security_door

class BalconyDoor(Door):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, tiltable: bool, room2 = None):
        super().__init__(posx, posy, width, height, room1, room2)
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.room1 = room1
        self.room2 = room2
        self.tiltable = tiltable

class House:
    def __init__(self):
        self.rooms = dict()

    def add_room(self, roomtoadd: Room):
        if roomtoadd.type not in self.rooms.keys():
            self.rooms[roomtoadd.type] = [roomtoadd]
        else:
            self.rooms[roomtoadd.type].append(roomtoadd)

    def get_window_area_facing_orientation(self, orientation: str):
        windowarea = 0

        selfroomslist = list(self.rooms.values())
        for lists in range(len(selfroomslist)):
            for rooms in selfroomslist[lists]:
                #print(rooms.openings)
                for key, value in rooms.openings.items():
                    if key == orientation:
                        for op in value:
                            if isinstance(op, Window):
                                windowarea += op.height * op.width
        return windowarea

    def get_number_of_openings_in_room_type(self, type: str) -> int:
        counter = 0

        selfroomslist = list(self.rooms.values())
        # print(selfroomslist)
        for lists in range(len(selfroomslist)):
            for rooms in selfroomslist[lists]:
                if rooms.type == type:
                    #print(rooms.openings)
                    #print(list(rooms.openings.values()))
                    for i in list(rooms.openings.values()):
                        counter += len(i)
        return counter

    def get_all_connected_rooms(self, room: Room) -> List[Room]:
        connected_rooms = []
        #print(list(room.openings.values()))
        for op in list(room.openings.values()):
            #print(op)
            for opop in op:
                connected_rooms.append(opop.room1)
                #print(connected_rooms)
                connected_rooms.append(opop.room2)
                #print(connected_rooms)
        # print(connected_rooms)
        connected_rooms.remove(None)
        connected_rooms = list(set(connected_rooms))
        # print(connected_rooms)
        connected_rooms.remove(room)
        #print(connected_rooms)
        return connected_rooms


if __name__ == '__main__':
    pass
    # corridor = Room("CORRIDOR", 15);
    # master_bed = Room("BEDROOM", 13);
    # second_bed = Room("BEDROOM", 11);
    # eatin_kitchen = Room("EATINKITCHEN", 27);
    # eatin_kitchen.add_opening("EAST", Window(20, 30, 50, 100, True))
    # eatin_kitchen.add_opening("NORTH", Window(20, 30, 50, 100, True))
    # #print(eatin_kitchen.openings)
    # master_bed.add_opening("NORTH", Window(22, 30, 50, 100, True))
    # second_bed.add_opening("WEST", Window(25, 30, 50, 100, True))
    # #print(master_bed.openings)
    # #print(second_bed.openings)
    # corridor.add_opening("EAST", HouseDoor(20, 40, 100, 200, corridor, True))
    # #print(corridor.openings)
    #
    # d = Door(20, 30, 90, 200, corridor, eatin_kitchen)
    # corridor.add_opening("EAST", d)
    # eatin_kitchen.add_opening("WEST", d)
    #
    # d = Door(40, 30, 90, 200, master_bed, corridor)
    # corridor.add_opening("WEST", d)
    # master_bed.add_opening("EAST", d)
    # d = Door(70, 30, 90, 200, second_bed, corridor)
    # corridor.add_opening("WEST", d)
    # second_bed.add_opening("EAST", d)
    #
    # h = House()
    # h.add_room(corridor);
    # h.add_room(master_bed);
    # h.add_room(second_bed);
    # h.add_room(eatin_kitchen);
    # # print(corridor.type)
    # # print(h.rooms.keys())
    # #print(h.rooms)
    # #h.get_window_area_facing_orientation("NORTH")
    # #h.get_number_of_openings_in_room_type("BEDROOM")
    # #h.get_all_connected_rooms(corridor)
