
CurrentRooms = []

class Room:

    def __init__(self, roomId):
        self.roomId = roomId
        self.usersInRoom = []

    def AddUser(self, user):
        self.usersInRoom.append(user)
        user.roomObject = self
    
    def RemoveUser(self, user):
        self.usersInRoom.remove(user)


def SearchRoom(user, idR):
    for room in CurrentRooms:
        if room.roomId == idR:
            room.AddUser(user)
            return True
    newRoom = Room(idR)
    CurrentRooms.append(newRoom)
    newRoom.AddUser(user)
    return False