

class User:

    def __init__(self, client, name, roomId, adress):
        self.client = client
        self.username = name
        self.inRoom = roomId
        self.adress = adress
        self.roomObject = None