class Server:
    def __init__(self, name):
        self.name = name

server1 = Server("DC01")
server2 = Server("FS01")

print(server1.name)
print(server2.name)


class Friends:
    total_friends = 0

    def __init__(self, name, place):
        self.name = name
        self.place = place

        Friends.total_friends += 1

    def move(self, new_place):
        self.place = new_place

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm from {self.place}.")


friend1 = Friends("Jimmy", 'Conroe')
friend2 = Friends("Tom", 'Houston')
friend3 = Friends("Charlie", 'Dallas')

friend1.introduce()
friend2.introduce()
friend3.introduce()

friend1.move('Austin')

print(Friends.total_friends)

print(friend1.name, friend1.place)
print(friend2.name, friend2.place)