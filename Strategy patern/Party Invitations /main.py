class Friend:
    def __init__(self, name):
        self.name = name
        self.last_invite = None

    def showInvite(self, invite):
        if self.last_invite:
            return self.last_invite
        return "No party"



class Party:
    def __init__(self, place):
        self.listOfFriends = []
        self.party = place

    def addFriend(self, friend):
        if friend not in self.listOfFriends:
            self.listOfFriends.append(friend)

    def deleteFriend(self, friend):
        if friend in self.listOfFriends:
            self.listOfFriends.remove(friend)

    def sendInvites(self):
        for friend in self.listOfFriends:
            friend.last_invite = self.party


party = Party("Bar")

Jhon = Friend("Jhon")
Mary = Friend("Mary")

party.addFriend(Jhon)
party.addFriend(Mary)

party.sendInvites()

print(Jhon.showInvite(party))
print(Mary.showInvite(party))

party.deleteFriend(Jhon)

party.party = ("Cafe")
party.sendInvites()

print(Jhon.showInvite(party))
print(Mary.showInvite(party))